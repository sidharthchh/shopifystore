from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
# always default to local. QA/Production must be explicit
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings.local')

app = Celery('store')

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
