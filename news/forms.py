from django import forms
from .models  import Advertisment
class AdvertiseForm(forms.ModelForm):
    class Meta:
        model=Advertisment
        fields='__all__'