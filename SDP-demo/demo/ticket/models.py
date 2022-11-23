from django.db import models
from django.contrib import admin
# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length = 50)
    created_date = models.DateTimeField(auto_now_add = True)
    description = models.CharField(max_length = 2000)
    department = models.CharField(max_length = 30)
    student = models.CharField(max_length = 30)
    issolved = models.IntegerField()
admin.site.register(Ticket)