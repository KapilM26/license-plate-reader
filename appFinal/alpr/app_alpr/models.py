from django.db import models

# Create your models here.
class Appdata(models.Model):
    name= models.CharField(max_length =200)
    email= models.EmailField(max_length=200, unique = True)
    vehicleNumber = models.CharField(max_length=100)
   
def __str__(self):
    return self.name 

class AppUsers(models.Model):
    userName = models.CharField(max_length =100)
    password = models.CharField(max_length=100)