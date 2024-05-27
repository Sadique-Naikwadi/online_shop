from django.urls import path,include
from .import views
app_name = 'usercart'

urlpatterns = [
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('cart_details/', views.cart_details, name='cart_details'),
    path('confirm_purchase/', views.confirm_purchase, name='confirm_purchase'),
    
]