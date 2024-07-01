from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItems
from .forms import OrderForm
from cart.cart import Cart

# Create your views here.

def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItems.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

            cart.clear()
            request.session['order_id'] = str(order.id)
                 
            return redirect(reverse('payment:process'))
            # context = {'order': order}
            # return render(request, 'orders/order_success.html', context)

    else:
        form = OrderForm()
    context = {'cart': cart, 'form': form}
    return render(request, 'orders/create_order.html', context)

