from django.forms import ModelForm
from django import forms
from .models import Shop,Product

class ShopForm(ModelForm):
    class Meta:
        model=Shop
        fields=['shopName','adress']
        labels={'shopName':('shop Name'),'adress':('Address')}
        help_texts={'shopName':'enter the name of your business','adress':'enter th address where your shop found'}
        widgets = {
            'shopName': forms.TextInput(attrs={'class': 'form-input-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-input-control'}),
           }
class ProductAdminForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = '__all__'

     def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['shop'].queryset = Shop.objects.filter(owner=user)