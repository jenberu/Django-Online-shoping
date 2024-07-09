from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['first_name','last_name','image','bio']  
        labels={'image':('profile Image'),'bio':('Biography') } 
        widgets={
              'bio':forms.Textarea({
                  'class':'input-control',
                  'placeholder':'Tell Us about your self',
                  'rows':5,
                  'cols':50,

              }),
              'first_name':forms.TextInput({
                  'class':'input-control',
                 'placeholder':'Fist Name',
              }),
               'last_name':forms.TextInput({
                  'class':'input-control',
                 'placeholder':'Last Name',
              }),

        }         