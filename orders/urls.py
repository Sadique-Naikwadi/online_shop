from django.urls import path,include
from .import views
from django.utils.translation import gettext_lazy as _
app_name = 'orders'

urlpatterns = [
    path('create_order/', views.create_order, name='create_order'),
    
    
]