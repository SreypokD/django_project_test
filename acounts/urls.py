from django.urls import path
from . import views
urlpatterns = [
    path('/home', views.homePage),
    path('product/' , views.productPage),
    path('customer/' , views.customerPage)
]
