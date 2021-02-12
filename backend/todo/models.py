from django.db import models


class TasksList(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    task_list = models.ForeignKey(TasksList, related_name='tasks', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    is_done = models.BooleanField(default=0)

    def __str__(self):
        return self.description
