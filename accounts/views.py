from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import UserCreateForm,UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import  login_required
from .models import UserProfile
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def signupaccount(request):
 if request.method == 'GET':
   return render(request, 'signupaccount.html', {'form':UserCreateForm()})
 else:
     password1=request.POST['password1']
     password2=request.POST['password2']
     username=request.POST['username']

     if password1==password2:
            
            try:
                user =User.objects.create(username=username) 
                user.save()
                login(request, user)
                return redirect('shop:product_list')
            except IntegrityError:
               return render(request, 'signupaccount.html', {'form':UserCreateForm(), 'error':_('Username already taken. Choose new username.')})

     else:
         return render(request, 'signupaccount.html', {'form':UserCreateForm(),'error': _('Passwords do not match')})
@login_required
def logoutaccount(request):
     #call logout and redirect to go back to the home page
     logout(request)
     return redirect('shop:product_list')   
def loginaccount(request):
     if request.method == 'GET':
          return render(request,'loginaccount.html', {'form':AuthenticationForm}) 
     
     else:
          user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
          if user is None:
               return render(request,'loginaccount.html', {'form':AuthenticationForm,'error': _('username and password do not match')}) 
          else:
               login(request,user)
               return redirect('shop:product_list')
@login_required          
def update_profile(request):
    if request.method=='GET':
        return render(request,'user_profile.html',{'form':UserProfileForm()})
    else:
        form=UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user_profile= UserProfile.objects.get(user=request.user)
            user_profile.first_name=form.cleaned_data['first_name']
            user_profile.last_name=form.cleaned_data['last_name']
            user_profile.image=form.cleaned_data['image']
            user_profile.bio=form.cleaned_data['bio']
            user_profile.save()
            return redirect('shop:product_list')
        else:
           return render(request,'userprofile.html',{'form':UserProfileForm(),'error':_('Pleace Insert correct data')})
def resset_password(request):
    if request.method=='GET':
        return render(request,'pass_resset.html')
    else:
        username=request.POST['username']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']
        if new_password==confirm_password:
            try:
                user=User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                messages.success(request,_('Password has been reset successfully.'))
                return redirect('loginaccount')
            except User.DoesNotExist:
                 messages.error(request, _('User with the given username does not exist. '))
                 return redirect('resset_passowrd')
        else: 
          messages.error(request, _('New password and confirm password do not match.'))
          return redirect('resset_passowrd')
              
                
                
                

            

              




# Create your views here.
