from django.db import models
from public.models import User
from django.contrib import admin

# Create your models here.
class Admins(User):
    department = models.CharField(max_length = 30)

admin.site.register(Admins)