from django.conf import settings
from shop.models import Product
from decimal import Decimal

class Cart:
    
    def __init__(self, request):
        self.session = request.session

        self.cart = self.session.get(settings.CART_SESSION_ID)
        if not self.cart:
            self.cart = {}
            self.session[settings.CART_SESSION_ID] = self.cart
        
        # self.session = request.session
        # self.cart = self.session.get(settings.CART_SESSION_ID, {})

    def add(self, product, quantity=1):
        
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}
            

        else:
            self.cart[product_id]['quantity'] = quantity

        
        self.save()

    def update(self,product,quantity):
        
        product_id = str(product.id)
        self.cart[product_id]['quantity'] = quantity
        self.save()
        return self.cart
    

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            return self.cart
        
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
    

        cart = self.cart.copy()
        for product in products:
            self.cart[str(product.id)]['product'] = product
    
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
    
    def __len__(self):

        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
    
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    


    # def clear(self):
    #     del self.session[settings.CART_SESSION_ID]
    #     self.save()
    
      
    
        
    def clear(self):
        if settings.CART_SESSION_ID in self.session:
            del self.session[settings.CART_SESSION_ID]
            self.session.modified = True
        
    
