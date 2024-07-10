from django.urls import path,include
from .import views
from django.utils.translation import gettext_lazy as _
app_name = 'cart'

urlpatterns = [
    path(_('add_to_cart/'), views.add_to_cart, name='add_to_cart'),
    path(_('remove_from_cart/'), views.remove_from_cart, name='remove_from_cart'),
    path(_('cart_details/'), views.cart_details, name='cart_details'),
    path(_('update_purchase/'), views.update_purchase, name='update_purchase'),
    
]