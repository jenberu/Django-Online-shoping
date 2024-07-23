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
 'delivery_date',
 ]
        widgets={
          'delivery_date':forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'dd/mm/yy'}),
          }       
class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['status']        
