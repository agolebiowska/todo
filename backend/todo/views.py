from django.views.decorators.csrf import csrf_exempt

from .models import TasksList
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TasksListSerializer
from rest_framework.response import Response
from rest_framework import status


class TaskListsViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows task lists to be created, read, updated or deleted.
    """
    queryset = TasksList.objects.all()
    serializer_class = TasksListSerializer
    permission_classes = [permissions.IsAuthenticated]

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

