from django.urls import  path
from tasks.views import RunDeleteExpiredTasksView, RunSendRemindersView



urlpatterns = [
    path('delete-expired/', RunDeleteExpiredTasksView.as_view(), name='delete-expired'),
    path('send-reminders/', RunSendRemindersView.as_view(), name='send-reminders'),
]