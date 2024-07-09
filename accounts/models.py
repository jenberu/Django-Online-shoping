from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    image=models.ImageField(upload_to='profile/image/',blank=True)
    first_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=30,blank=True)
    bio=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.first_name + self.last_name
