from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.exceptions import ValidationError
import uuid


# Create your views here.

def index(request, category_slug=None):
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,translations__language_code=language, translations__slug=category_slug)
        products = Product.objects.filter(category=category,available=True)
    else:
        products = Product.objects.filter(available=True)
    context = {'products': products}
    return render(request, 'shop/index.html', context)

def product_details(request,pk,slug):
    print('pk: ', pk)
    language = request.LANGUAGE_CODE
    try:
        pk = uuid.UUID(pk, version=4)
        product = get_object_or_404(Product, id=pk, translations__language_code=language, translations__slug=slug)
    except ValueError:
        raise ValidationError('Invalid UUID')

    context = {'product': product}
    return render(request, 'shop/product_details.html', context)
    

    
