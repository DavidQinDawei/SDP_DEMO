from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length= 100)
    email = models.CharField(max_length= 50)
    netid = models.CharField(max_length= 20)
    password = models.CharField(max_length= 30)
    isactive = models.IntegerField()