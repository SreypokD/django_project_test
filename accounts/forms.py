from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta: 
        model= User
        fields = ['username' , 'email' , 'password1' , 'password2']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' #take all feild of orders