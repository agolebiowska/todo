from rest_framework import permissions
from rest_framework import viewsets
from . import serializers
from . import models


class TaskListsViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows task lists to be created, read, updated or deleted.

    Get all tasks lists         GET /api/lists/
    Get single tasks list       GET /api/lists/:id/
    Create new tasks list       POST /api/lists/
    Update existing tasks list  PUT /api/lists/:id/
    Delete existing tasks list  DELETE /api/lists/:id/
    """
    queryset = models.TasksList.objects.all()
    serializer_class = serializers.TasksListSerializer
    # permission_classes = [permissions.IsAuthenticated] If we want to use basic auth


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows tasks to be created, read, updated or deleted.

    Get all tasks for a list    GET /api/lists/:id/tasks/
    Get single task for a list  GET /api/lists/:id/tasks/:id/
    Create new task             POST /api/lists/:id/tasks/
    Update existing task        PUT /api/lists/:id/tasks/
    Delete existing task        DELETE /api/lists/:id/tasks/
    """
    queryset = models.Task.objects.all().select_related('task_list')
    serializer_class = serializers.TaskSerializer
