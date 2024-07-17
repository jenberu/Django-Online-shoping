from django.shortcuts import render,redirect
from .models import New,Advertisment
from .forms import AdvertiseForm
def get_news(request):
    news=New.objects.all().order_by('-date')
    return render(request,'news.html',{'news':news})

def create_advertisement(request):
    if request.method=='GET':
        return render(request,'add/create_add.html',{'form':AdvertiseForm()})
    else:
        form=AdvertiseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')







# Create your views here.
