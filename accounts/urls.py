

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dasboardPage, name='home'),
    path('products/', views.productPage, name='product'),
    path('customers/<str:pk>/', views.customerPage, name='customer'),
    path('create-order/', views.createOrder, name='create-order'),
    path('update-order/<str:pk>/', views.updateOrder, name='update-order'),
    path('delete-order/<str:pk>/', views.deleteOrder, name='delete-order'),
    
]