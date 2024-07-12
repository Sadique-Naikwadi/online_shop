from django.db import models
from django.utils.text import slugify
import uuid
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        slug = models.SlugField(max_length=250, unique=True, blank=True),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)

    class Meta:
        # ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
            super(Category,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

    

class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        slug = models.SlugField(max_length=250, unique=True, blank=True),
        description = models.TextField(blank=True),
    )
    image = models.ImageField(upload_to='products/', blank=True, default='default.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)

    class Meta:
        # ordering = ['name']
        pass

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
            super(Product,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

