from django.urls import path
from public import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.userApi,name='public'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)