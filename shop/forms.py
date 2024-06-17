from django.forms import ModelForm
from django import forms
from .models import Shop

class ShopForm(ModelForm):
    class Meta:
        model=Shop
        fields=['shopName','adress']
        labels={'shopName':('shop Name'),'adress':('Address')}