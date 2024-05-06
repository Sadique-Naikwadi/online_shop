from django.urls import path,include
from .import views
app_name = 'usercart'

urlpatterns = [
    path('add_to_cart/<str:pk>/', views.add_to_cart, name='add_to_cart'),
    
]