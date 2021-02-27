from .models import TasksList, Task
from rest_framework import serializers

"""Define how our models can be serialized"""

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'is_done', 'task_list']


class TasksListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = TasksList
        fields = ['id', 'title', 'description', 'tasks']

