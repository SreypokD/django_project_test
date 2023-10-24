from django.shortcuts import render ,redirect
from .models import *
from .forms import *
from django.forms import inlineformset_factory #create mutiple fields 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
# I don't want to user see page without login
from django.contrib.auth.decorators import login_required
from .dicorators import unauthenticated_user ,admin_only,allowed_user
from django.contrib.auth.models import Group
# from django.http import HttpResponse

# Create your views here.
@login_required(login_url='login')
@admin_only
def dasboardPage(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_order = orders.count()
    total_product = Products.objects.all().count()
    total_delivered = orders.filter(status = 'Delivered').count()
    total_pending = orders.filter(status = 'Pending').count()

    context = {
        'customers': customers,
        'orders' : orders,
        'total_product' : total_product,
        'total_order' : total_order,
        'total_delivered': total_delivered,
        'total_pending' : total_pending,
    }
    return render(request, 'accounts/dasboard.html' ,context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def productPage(request):
    products = Products.objects.all()

    return render(request, 'accounts/product.html', {'products' : products})

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customerPage(request ,pk ):
        customers = Customer.objects.get(id =pk)
        orders = customers.order_set.all() #get order of cutomer 
        total_order = orders.count()
        form = OrderForm()
        # myfilter = OrderFilter()
        context = {
            'form': form,
            #  'myfilter' : myfilter,
             'customers': customers,
             'orders': orders,
             'total_order' : total_order,
        }
        return render(request, 'accounts/customer.html' , context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def createOrder(request):
         # 
    form = OrderForm()
    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    context = {
        'form' : form
    }
    return render(request, 'accounts/orderForm.html' , context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form': form,
        'order': order
    }
    
    return render(request, 'accounts/orderForm.html' ,context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    
    context = {
        'items' : order
    }
    
    return render(request, 'accounts/delete.html' ,context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def placeOrder(request ,pk):
    orderFormSet = inlineformset_factory(Customer, Order, fields=('products' , 'status') ,extra=5)
    customer = Customer.objects.get(id = pk)
    # form = OrderForm(initial={'customer' : customer}) #show name of customer
    formset =orderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == 'POST':
        print(request.POST)
        formset = orderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/') 
    context = {

        'formset' : formset,
        'customer' : customer
    }
    return render(request, 'accounts/placeOrder.html' , context)

@unauthenticated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            print(request.POST)
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                # relation user with cutomer when create new user
                Customer.objects.create(user=user)
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {username}')
                return redirect('/login') 
        context = {
            'form' : form
        }
        return render(request, 'accounts/register.html' , context)

@unauthenticated_user
def loginPage(request):
        if request.method == "POST":
            username = request.POST.get('username') #name of input 
            password = request.POST.get('password')
            # check in database
            user = authenticate(request , username = username , password = password)
            if user is not None:
                login(request , user)
                return redirect('/')
            else:
                messages.info(request ,f'Wrong Usernam or Password!')
        return render(request, 'accounts/login.html' )


def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def userPage(request):

    orders = request.user.customer.order_set.all()
    total_order = orders.count()
    total_product = Products.objects.all().count()
    total_delivered = orders.filter(status = 'Delivered').count()
    total_pending = orders.filter(status = 'Pending').count()
    context = {
        'orders': orders,
        'total_product' : total_product,
        'total_order' : total_order,
        'total_delivered': total_delivered,
        'total_pending' : total_pending,
    }
    return render(request, 'accounts/user.html' , context)




