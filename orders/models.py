from django.db import models
from shop.models import Product
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(_('first_name'),max_length=50)
    last_name = models.CharField(_('last_name'),max_length=50)
    email = models.EmailField(_('email'),max_length=254)
    address = models.CharField(_('address'),max_length=250)
    postal_code = models.CharField(_('postal_code'),max_length=20)
    city = models.CharField(_('city'),max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=250, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)

    class Meta:
        verbose_name_plural = 'OrderItems'
    
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
    


