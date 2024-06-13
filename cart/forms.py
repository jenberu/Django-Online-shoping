from django import forms
  #allows the user to select a quantity between 1 and 20
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)#coerce=int to convert the input into an integer
    override=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
