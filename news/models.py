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
    image=models.ImageField(blank=True,upload_to='advertisment/image/')  
    description=models.TextField(blank=True)
    url=models.URLField(blank=True)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    active=models.BooleanField(default=True)
    def __str__(self) :
        return self.title
    def is_active(self):
        return self.start_date <= timezone.now()<= self.end_date

    