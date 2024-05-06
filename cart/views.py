from django.shortcuts import render
from shop.models import Product
from .cart import Cart
from django.http import JsonResponse
import json

# Create your views here.

def add_to_cart(request, pk):

    if request.method == 'POST':
        data_dict = json.loads(request.body)
        product = data_dict['product']
        cart = Cart(request)
        cart.add(Product(product))


        dataToSend = {"total": len(cart)}
    return JsonResponse(dataToSend)


