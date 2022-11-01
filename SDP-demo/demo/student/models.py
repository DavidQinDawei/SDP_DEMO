from unittest.util import _MAX_LENGTH
from django.db import models
from public.models import User
from django.contrib import admin
# Create your models here.
class Student(User):
    major = models.CharField(max_length = 30)
    club = models.CharField(max_length = 30)
    year = models.CharField(max_length = 10)
admin.site.register(Student)
