

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dasboardPage, name='home'),
    path('products/', views.productPage, name='product'),
    path('customers/<str:pk>/', views.customerPage, name='customer'),
    path('create-order/', views.createOrder, name='create-order'),
    path('place-order/<str:pk>', views.placeOrder, name='place-order'),
    path('update-order/<str:pk>/', views.updateOrder, name='update-order'),
    path('delete-order/<str:pk>/', views.deleteOrder, name='delete-order'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('user/', views.userPage, name='user-page'),

    
]