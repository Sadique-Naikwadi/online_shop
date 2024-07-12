from django.urls import path,include, re_path
from .import views
from django.utils.translation import gettext_lazy as _

app_name ='shop'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(_(r'^(?P<pk>[^/]+)/(?P<slug>[\w-]+)/$'), views.product_details, name='product_details'),
]
