from .models import TasksList, Task
from rest_framework import serializers


class TasksListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TasksList
        fields = ['id', 'title', 'description']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'is_done', 'task_list']
