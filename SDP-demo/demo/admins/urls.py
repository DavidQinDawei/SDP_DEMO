from django.urls import path

from admins import admins_handler

urlpatterns = [
    # modify, delete, add
    path('users', admins_handler.admins_dispatcher),
    
]
