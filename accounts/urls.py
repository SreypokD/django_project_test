

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dasboardPage, name='home'),
    path('products/', views.productPage, name='product'),
    path('customers/<str:pk>/', views.customerPage, name='customer'),
]