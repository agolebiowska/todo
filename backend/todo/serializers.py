from .models import TasksList
from rest_framework import serializers


class TasksListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TasksList
        fields = ['id', 'title', 'description']
