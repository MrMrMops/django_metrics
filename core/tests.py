from django.test import TestCase
from unittest.mock import patch
# Create your tests here.

import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from core.models import Task

User = get_user_model()

@pytest.mark.django_db
def test_user_can_create_task():
    client = APIClient()
    user = User.objects.create_user(username='user1', password='pass')
    client.force_authenticate(user=user)

    response = client.post("/api/tasks/", {"title": "Test task"})
    assert response.status_code == 201
    assert Task.objects.filter(owner=user, title="Test task").exists()


@pytest.mark.django_db
def test_user_sees_only_own_tasks():
    user1 = User.objects.create_user(username='user1', password='pass')
    user2 = User.objects.create_user(username='user2', password='pass')

    assert User.objects.get(username='user1').username == user1.username

    Task.objects.create(owner=user1, title="User1 task")

    assert Task.objects.get(title='User1 task').owner_id == user1.id

    Task.objects.create(owner=user2, title="User2 task")

    client = APIClient()
    client.force_authenticate(user=user1)
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    assert len(response.json()['results']) == 1
    assert response.json()['results'][0]['title'] == 'User1 task' 
