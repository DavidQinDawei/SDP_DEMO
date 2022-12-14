from django.contrib import admin
from django.db import models
# Create your models here.
class Ticket(models.Model):
    description = models.CharField(max_length = 2000)
    department = models.CharField(max_length = 30)
    student =  models.CharField(max_length = 30)
    issolved = models.IntegerField()
    date = models.DateField()
admin.site.register(Ticket)