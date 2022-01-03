from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_jwt_capstone_backend.settings')
app = Celery('drf_jwt_capstone_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'America/Chicago'
 
app.autodiscover_tasks()
 
 