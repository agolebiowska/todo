from .models import TasksList, Task
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'is_done', 'task_list']


class TasksListSerializer(serializers.HyperlinkedModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = TasksList
        fields = ['id', 'title', 'description', 'tasks']

