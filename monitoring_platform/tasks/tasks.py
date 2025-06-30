from celery import shared_task
from datetime import datetime
from core.models import Task

@shared_task
def delete_expired_tasks():
    Task.objects.filter(deadline__lt=datetime.now(), is_done=False).delete()

@shared_task
def send_task_reminders():
    # Заглушка: логика рассылки email уведомлений
    print("Уведомления разосланы")
