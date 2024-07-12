from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Category,Product

# Register your models here.
class CategoryAdmin(TranslatableAdmin):
    pass

class ProductAdmin(TranslatableAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

