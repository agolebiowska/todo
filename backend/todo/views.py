from django.views.decorators.csrf import csrf_exempt

from .models import TasksList, Task
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TasksListSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status


class TaskListsViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows task lists to be created, read, updated or deleted.
    """
    queryset = TasksList.objects.all()
    serializer_class = TasksListSerializer
    # permission_classes = [permissions.IsAuthenticated] If we want to use basic auth credentials

    """
    Get all tasks lists     GET /api/lists/
    Get single tasks list   GET /api/lists/:id/
    """
    @csrf_exempt
    def get(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Create new tasks list  POST /api/lists/
    """
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    """
    Update existing tasks list  PUT /api/lists/:id/
    """
    @csrf_exempt
    def put(self, request):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update()
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Delete existing tasks list  DELETE /api/lists/:id/
    """
    @csrf_exempt
    def delete(self, request):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows tasks to be created, read, updated or deleted.
    """
    queryset = Task.objects.all().select_related('task_list')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    """
    Get all tasks for a list    GET /api/lists/:id/tasks/
    Get single task for a list  GET /api/lists/:id/tasks/:id/
    """
    @csrf_exempt
    def get(self, request):
        task_list_id = self.kwargs.get("list_pk")
        queryset = self.queryset.filter(task_list_id=task_list_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Create new task  POST /api/lists/:id/tasks/
    """
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    """
    Update existing task  PUT /api/lists/:id/tasks/
    """
    @csrf_exempt
    def put(self, request):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update()
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Delete existing task  DELETE /api/lists/:id/tasks/
    """
    @csrf_exempt
    def delete(self, request):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
