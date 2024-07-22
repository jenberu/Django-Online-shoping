from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):

    
    class Meta:
        model=Order
        fields = [
 'first_name',
 'last_name',
 'email',
 'phone_number',
 'address',
 'postal_code',
 'city',
 ]
        
class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['status']        
