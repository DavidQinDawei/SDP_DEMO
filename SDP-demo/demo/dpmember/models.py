from django.db import models
from public.models import User
from django.contrib import admin
# Create your models here.
class dpmember(User):
    department = models.CharField(max_length = 30)
admin.site.register(dpmember)