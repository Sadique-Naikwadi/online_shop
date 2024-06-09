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


def remove_from_cart(request):
    if request.method == 'POST':
        data_dict = json.loads(request.body)
        product_id = data_dict['product_id']
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        result = cart.remove(product=product)
        dataToSend = {"result": result}
    return JsonResponse(dataToSend)

def confirm_purchase(request):
    cart = Cart(request)
    if request.method == 'POST':
        data_dict = json.loads(request.body)
        product_id = str(data_dict['product_id'])
        product_quantity = int(data_dict['select_quantity'])
        print('product quntity: ', product_quantity)
        product = Product.objects.get(id=product_id)
        print(product)
        cart = cart.update(request,product,product_quantity)
        
        
    
    
    context = {'cart': cart}
    return render(request, 'cart/confirm_purchase.html', context)




def cart_details(request):
    
    cart = Cart(request)
    context = {'cart': cart}
    return render(request,'cart/cart_details.html', context)

