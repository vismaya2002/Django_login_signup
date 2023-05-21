from django.db import models

# Create your models here.

class Details(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20)
    email  = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    district = models.CharField(max_length=20)
    city  = models.CharField(max_length=20)
    
class Otp(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    otp = models.IntegerField(default=0)