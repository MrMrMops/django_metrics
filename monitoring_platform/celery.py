import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring_platform.settings')

app = Celery('task_manager')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'