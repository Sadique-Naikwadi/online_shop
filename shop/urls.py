from django.urls import path,include
from .import views

app_name ='shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/<slug:slug>/', views.product_details, name='product_details'),
]
