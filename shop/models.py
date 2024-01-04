from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Category,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

    

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, default='default.jpg')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)

    class Meta:
        ordering = ['name']

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Product,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

