from django.db import models

# Create your models here.
class Customer(models.Model) :
    name  = models.CharField(max_length= 200 , null= True )#if not complete )
    phone = models.CharField(max_length=200 , null=True)
    email = models.CharField(max_length=200 , null=True)
    date_created = models.DateTimeField(auto_now_add=True , null= True)

# run command to create :  python manage.py makemigrations
    def __str__(self):
        return self.name
    
class Tag(models.Model) :
    name  = models.CharField(max_length= 200 , null= True )#if not complete )
    def __str__(self):
        return self.name
    
# create productable
class Products(models.Model):
    CATEGORY = (
        ('in door' , 'in door'),
        ('out door' , 'out door')
    )

    name = models.CharField(max_length=200 , null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200 , null=True , choices=CATEGORY)
    description = models.CharField(max_length=200 , null=True , blank=True)
    date_created = models.DateTimeField(auto_now_add=True , null=True)
    tag = models.ManyToManyField(Tag)  # relation many to many

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('out for b' , 'out for b'),
        ('Delivered' , 'Delivered')
    )
    # relation one to one
    customer = models.ForeignKey(Customer, null=True , on_delete=models.SET_NULL ) # ondelete still set value but equal ''
    products = models.ForeignKey(Products, null=True , on_delete=models.SET_NULL )

    status = models.CharField(max_length=200 , null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True , null= True)

    def __str__(self):
        return self.status