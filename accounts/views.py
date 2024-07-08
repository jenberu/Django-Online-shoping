from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import  login_required

def signupaccount(request):
 if request.method == 'GET':
   return render(request, 'signupaccount.html', {'form':UserCreateForm()})
 else:
     form = UserCreateForm(request.POST)
     if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('shop:product_list')
            except IntegrityError:
               return render(request, 'signupaccount.html', {'form':UserCreateForm(), 'error':'Username already taken. Choose new username.'})

     else:
         return render(request, 'signupaccount.html', {'form':UserCreateForm(),'error': 'Passwords do not match' if 'password1' in form.errors else 'Please correct the error(s) below.'})
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
               return render(request,'loginaccount.html', {'form':AuthenticationForm,'error': 'username and password do not match'}) 
          else:
               login(request,user)
               return redirect('shop:product_list')




# Create your views here.
