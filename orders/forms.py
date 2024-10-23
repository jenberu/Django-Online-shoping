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
 'house_no',
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
            'house_no':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'House No if you have'}),
            'city':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'City'}),



          }       
class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['status']        
