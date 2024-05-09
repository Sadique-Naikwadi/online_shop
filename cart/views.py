from django.shortcuts import render
from shop.models import Product
from .cart import Cart
from django.http import JsonResponse
import json

# Create your views here.

def add_to_cart(request):

    if request.method == 'POST':
        data_dict = json.loads(request.body)
        product_id = data_dict['product_id']
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        cart.add(product=product)
        dataToSend = {"total": len(cart)}

    return JsonResponse(dataToSend)


def cart_details(request):
    
    cart = Cart(request)
    context = {'cart': cart}
    return render(request,'cart/cart_details.html', context)

