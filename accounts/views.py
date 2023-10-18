from django.shortcuts import render
from .models import *
# from django.http import HttpResponse

# Create your views here.
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
        'total_pending' : total_pending
    }
    return render(request, 'accounts/dasboard.html' ,context)

def productPage(request):
    products = Products.objects.all()

    return render(request, 'accounts/product.html', {'products' : products})

def customerPage(request ,pk ):
        customers = Customer.objects.get(id =pk)
        orders = customers.order_set.all() #get order of cutomer 
        total_order = orders.count()
        context = {
             'customers': customers,
             'orders': orders,
             'total_order' : total_order
        }
        return render(request, 'accounts/customer.html' , context)
