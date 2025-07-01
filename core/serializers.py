from rest_framework import serializers

from core.models import Task


from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'is_completed', 'created_at')

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Заголовок должен быть не короче 3 символов.")
        return value