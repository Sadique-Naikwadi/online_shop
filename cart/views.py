from django.shortcuts import render
from shop.models import Product
from .cart import Cart
from django.utils.translation import gettext_lazy as _
import uuid
import json
from django.http import JsonResponse
from django.core.exceptions import ValidationError


# Create your views here.

def add_to_cart(request):

    if request.method == 'POST':
        
        data = json.loads(request.body)
        product_id=data.get('product_id')
        # product_id = request.GET.get('product_id')
        # print('product_id: ', product_id)

        try:
            product_id = uuid.UUID(product_id, version=4)
            product = Product.objects.get(id=product_id)
            print('product: ', product)
        except ValueError:
            raise ValidationError('invalid UUID')

        cart = Cart(request)
        cart.add(product=product)
        dataToSend = {"total": len(cart.cart)}
        print('data:', dataToSend)
        

    return JsonResponse(dataToSend)


def remove_from_cart(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        product_id=data.get('product_id')
        try:

            product_id = uuid.UUID(product_id, version=4)
            product = Product.objects.get(id=product_id)

        except ValueError:

            raise ValidationError('invalid UUID')
        
        cart = Cart(request)
        cart.remove(product=product)
        dataToSend = {'status': 'success', 'cart': len(cart.cart)}
    return JsonResponse(dataToSend)

def update_purchase(request):
    print('before get: ', request)
    cart = Cart(request)
    if request.method == 'POST':
        
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('select_quantity')

        if product_id and quantity:
            print('enter in if statment')

            try:

                product_id = uuid.UUID(product_id, version=4)
                product = Product.objects.get(id=product_id)

            except ValueError:

                raise ValidationError('invalid UUID')
            
            # cart.update(product,product_quantity)
            print('Cart before update: ', cart.cart)
            cart.update(product,int(quantity))
            print('Cart after update: ', cart.cart)
            return JsonResponse({'status': 'success', 'cart': cart.cart})


        
    print('cart in context: ', cart.cart)
    context = {'cart': cart}
    return render(request, 'cart/confirm_purchase.html', context)       
    




def cart_details(request):
    
    cart = Cart(request)
    context = {'cart': cart}
    return render(request,'cart/cart_details.html', context)

