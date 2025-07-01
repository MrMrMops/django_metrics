from celery import shared_task
from datetime import datetime
from core.models import Task

@shared_task
def delete_expired_tasks():
    Task.objects.filter(is_completed=False).delete()

@shared_task
def send_task_reminders():
    # Заглушка: логика рассылки email уведомлений
    print("Уведомления разосланы")

from celery import shared_task
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

@shared_task
def my_periodic_task():
    logger.info(f"Task run at {datetime.now()}")