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
           'last_name':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Last Name'}),
            'first_name':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'First Name'}),
           'email':forms.EmailInput(attrs={ 'class': 'form-control', 'placeholder': 'Email'}),
           'phone_number':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'adress'}),
            'postal_code':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Postal Code'}),
            'city':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'City'}),



          }       
class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['status']        
