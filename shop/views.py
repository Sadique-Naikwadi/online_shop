from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.filter(available=True)
    context = {'products': products}
    return render(request, 'shop/index.html', context)
