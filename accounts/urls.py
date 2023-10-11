from django.urls import path
from . import views
urlpatterns = [
    path('', views.dasboardPage),
    # path('products/' , views.productPage),
    # path('customers/' , views.customerPage)
]