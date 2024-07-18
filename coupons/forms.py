from django import forms
from django.utils.translation import gettext_lazy as _

class CouponForm(forms.Form):
    code=forms.CharField(label=_('Apply for Discount'),widget=forms.TextInput(attrs={'class':'coupoun-input','placeholder':'enter code'}))
