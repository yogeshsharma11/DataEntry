from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)  
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    country = models.CharField(max_length=100)


    def __str__(self):
        return self.name
