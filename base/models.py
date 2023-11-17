from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    body = models.TextField()


class Clients(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    client_id = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15,default="") 
    age = models.CharField(max_length=5,default='10') 
    sex = models.CharField(max_length=5,default='male') 
