from django.urls import path,include
from .import views
app_name = 'usercart'

urlpatterns = [
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart_details/', views.cart_details, name='cart_details'),
    
]