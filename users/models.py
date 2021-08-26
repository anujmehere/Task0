from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50,default='')
    lastname=models.CharField(max_length=50,default='')
    email=models.EmailField(max_length=50,default='')
    username=models.CharField(max_length=50,default='')
    password=models.CharField(max_length=50,default='')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE,default='1')
    title=models.CharField(max_length=50,default='')
    text=models.TextField(max_length=1500,default='')
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.title