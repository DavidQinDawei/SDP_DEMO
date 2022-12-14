from django.db import models

from django.contrib import admin
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length= 100)
    email = models.CharField(max_length= 50)
    netid = models.CharField(max_length= 20)
    password = models.CharField(max_length= 30)
    isactive = models.IntegerField()
    type = models.CharField(max_length=30, blank= True,null=True)
    department = models.CharField(max_length = 30, blank= True, null=True)
    major = models.CharField(max_length = 30, blank= True, null=True)
    club = models.CharField(max_length = 30, blank= True, null=True)
    year = models.CharField(max_length = 10, blank= True, null=True)
admin.site.register(Users)