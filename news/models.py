from django.db import models
from django.utils import timezone

class New(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    

class Advertisment(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    url=models.URLField(blank=True)
    image=models.ImageField(blank=True,upload_to='advertisment/image/')  

    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    active=models.BooleanField(default=True)
    def __str__(self) :
        return self.title
    def is_active(self):
        return self.start_date <= timezone.now()<= self.end_date
    
class AddsImage(models.Model):
    adds=models.ForeignKey(Advertisment,on_delete=models.CASCADE,related_name='images') 
    image=models.ImageField(blank=True,upload_to='advertisment/image/')  
    def __str__(self) :
        return str(self.id)

       

    