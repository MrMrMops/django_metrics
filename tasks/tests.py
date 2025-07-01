from django.test import TestCase
from django.contrib.auth import get_user_model
import pytest
from rest_framework.test import APIClient
from unittest.mock import Mock, patch


from tasks.tasks import delete_expired_tasks
from core.models import Task
from datetime import timedelta
from django.utils import timezone



User = get_user_model()

@pytest.mark.django_db
def test_admin_can_trigger_delete_expired_task():
    user = User.objects.create_superuser(username='admin', password='pass')
    client = APIClient()
    client.force_authenticate(user=user)

    # Создаем мок с id
    mock_result = Mock()
    mock_result.id = "fake-task-id"

    with patch("tasks.views.delete_expired_tasks.delay", return_value=mock_result):
        response = client.post("/run/delete-expired/")
        assert response.status_code == 200
        assert response.json()["task_id"] == "fake-task-id"


@pytest.mark.django_db
def test_non_admin_cannot_trigger_delete_expired_task():
    user = User.objects.create_user(username='user', password='pass')
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.post("/run/delete-expired/")
    assert response.status_code == 403

@pytest.mark.django_db
def test_delete_expired_tasks():
    user = User.objects.create_user(username="testuser", password="pass")

    # Создаем задачу, у которой дата устарела
    expired = Task.objects.create(
        title="Expired",
        owner=user,
        created_at="2024-01-01T00:00:00Z",  # или datetime.datetime(...) — главное, чтобы прошло больше N дней
    )

    # Запускаем Celery-задачу
    delete_expired_tasks()

    # Проверяем, что задача удалена
    assert not Task.objects.filter(id=expired.id).exists()