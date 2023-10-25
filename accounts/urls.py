from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('reset_password/' , auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html') , name='password_reset'),
    path('reset_password_send/' , auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_send.html') , name= 'password_reset_done'),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_form.html'), name= 'password_reset_confirm'),
    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_done.html') , name='password_reset_complete'),
    
]