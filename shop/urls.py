from django.urls import path,include
from .import views
from django.utils.translation import gettext_lazy as _

app_name ='shop'

urlpatterns = [
    path('', views.index, name='index'),
    path(_('<str:pk>/<slug:slug>/'), views.product_details, name='product_details'),
]
