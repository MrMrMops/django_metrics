from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser  # или ваша логика доступа
from .tasks import delete_expired_tasks, send_task_reminders


class RunDeleteExpiredTasksView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        result = delete_expired_tasks.delay()
        return Response({"task_id": result.id, "status": "task started"})


class RunSendRemindersView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        result = send_task_reminders.delay()
        return Response({"task_id": result.id, "status": "task started"})
