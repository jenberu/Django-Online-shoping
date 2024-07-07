from django.urls import path
from . import views ,stripewebhooks


app_name='payment'


urlpatterns=[
    path('process/',views.payment_procces,name='paymentprocces'),
    path('completed/',views.payment_completed,name='completed'),
    path('canceled/',views.payment_canceled,name='canceled'),
    path('webhook/', stripewebhooks.stripe_webhook, name='stripe-webhook'),
    path('onwer_process/',views.shop_onwer_payemnet_procces,name='onwer_payment_procces'),
    path('success/',views.onwer_payment_success,name='onwer_completed'),
    path('cancele/',views.onwer_payment_cancele,name='onwer_canceled'),


]
