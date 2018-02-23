from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
import os

urlpatterns = [
    url(r'^api/', include('rpg.urls')),
]

enable_admin = os.environ.get('DJANGO_ADMIN', False) == 'True'

if enable_admin:
    urlpatterns.append(path('admin/', admin.site.urls))
