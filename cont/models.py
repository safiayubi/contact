from email import message
from django.db import models

# Create your models here.

class contact(models.Model):

    name= models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    message= models.TextField(max_length=50)


