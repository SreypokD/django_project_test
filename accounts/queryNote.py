#1 open shell to  allows us to interact with our Django application and its components
        #c  python manage.py shell
#2 import model of app 
        #c from accounts.models import *
#3 return all customer from customer table
customer = Customer.objects.all()
#4 return first cutomer in table
firstCustomer = Customer.objects.first()
#4 return last cutomer in table 
lastCustomer = Customer.objects.last()
#5 return single customer by name
customerByName = Customer.objects.get(name='SreypokDoem')
#6 return single cutomer by ID
customerById = Customer.objects.get(id=4)
#7 return order relate to customer  ()
order = customer.order_set.all()
# return value of product
products = Products.objects.filter(Category = 'in door')
# return short by of order by id
leastToGreatest = Products.objects.all().order_by('id')
greatestToLeast = Products.objects.all().order_by('-id')
# query many to many filed of tag
products = Products.objects.filter(tag__name = 'gym')
