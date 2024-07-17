from django import forms
from .models  import Advertisment
class AdvertiseForm(forms.ModelForm):
    class Meta:
        model=Advertisment
        fields = ['title', 'image', 'url', 'start_date', 'end_date']
