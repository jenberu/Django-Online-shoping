from django.urls import path
from . import views

app_name='payment'


urlpatterns=[
    path('process/',views.payment_procces,name='paymentprocces'),
    path('completed/',views.payment_completed,name='completed'),
    path('canceled/',views.payment_canceled,name='canceled'),
]