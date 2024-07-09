from django.shortcuts import render
from .models import New

def get_news(request):
    news=New.objects.all().order_by('-date')
    return render(request,'news.html',{'news':news})


# Create your views here.
