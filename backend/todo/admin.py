from django.contrib import admin

from .models import TasksList
from .models import Task

admin.site.register(TasksList)
admin.site.register(Task)
