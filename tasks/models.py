from django.db import models

from categories.models import Category

# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False,)
    task_assign_date = models.DateTimeField()
    category = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return self.taskTitle
