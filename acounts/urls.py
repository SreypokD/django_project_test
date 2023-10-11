from django.urls import path
from . import views
urlpatterns = [
    path('/home', views.homePage),
    path('products/' , views.productPage),
    path('customers/' , views.customerPage)
]
