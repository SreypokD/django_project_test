from django.urls import path
from . import views
urlpatterns = [
    path('dasboard/', views.dasboardPage),
    # path('products/' , views.productPage),
    # path('customers/' , views.customerPage)
]