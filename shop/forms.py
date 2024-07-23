from django import forms
from .models import Shop,Product,SocialMedia

class ShopForm(forms.ModelForm):
    class Meta:
        model=Shop
        fields=['shopName','adress','contact_number']
        labels={'shopName':('shop Name'),'adress':('Address'),'contact_number':('phone number')}
        help_texts={'shopName':'enter the name of your business','adress':'enter th address where your shop found'}
        widgets = {
            'shopName': forms.TextInput(attrs={'class': 'form-input-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-input-control'}),
            'contact_number':forms.TextInput(attrs={'class': 'form-input-control'}),
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
class SocialMediaForm(forms.ModelForm):
    class Meta:
        model=SocialMedia        
        fields=['shop','facebook_url','twitter_url','instagram_url','telegram_url']
        widgets = {
            'shop': forms.Select(attrs={'class': 'form-control'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'if you have'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'if you have'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'if you have'}),
            'telegram_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'if you have'}),
        }

