from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePage),
    path('products/' , views.productPage),
    path('customers/' , views.customerPage)
]
