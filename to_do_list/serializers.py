from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_title(self, title):
        if len(title) < 5:
            raise ValidationError('title must be more than 5')
        return title

    def validate_description(self, description):
        if len(description) < 1000:
            raise ValidationError('description must be less than 1000')
        return description
