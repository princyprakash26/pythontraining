from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=123,default='')
    phone=models.CharField(default='',max_length=12)
    email=models.EmailField()
    description=models.TextField()