from django.db import models

# Create your models here.

class User(models.Model):
    # userId = models.IntegerField(max_length=10)
    emailId = models.EmailField(blank=True, unique=True)
    password = models.CharField(max_length=100)
    userName = models.CharField(max_length=50,default='USER')
    phoneNo = models.IntegerField(default=100)
