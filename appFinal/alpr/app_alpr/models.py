from django.db import models

# Create your models here.
class Appdata(models.Model):
    name= models.CharField(max_length =200)
    email= models.EmailField(max_length=200, unique = True)
    vehicleNumber = models.CharField(max_length=100)


def _str_(self):
    return self.name