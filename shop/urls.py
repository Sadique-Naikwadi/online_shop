from django.urls import path,include
from .import views

app_name ='shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category_slug>/', views.index, name='products_by_category'),
    path('<str:pk>/<slug:slug>/',views.product_details, name='product_details'),
]
