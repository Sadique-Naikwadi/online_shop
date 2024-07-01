from django.urls import path
from .import views
from .import webhooks
from django.utils.translation import gettext_lazy as _
app_name = 'payment'
urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('webhook/', webhooks.stripe_webhook, name='stripe-webhook'),
]