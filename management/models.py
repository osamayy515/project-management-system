from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(User, related_name='project_users')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('INPROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='TODO')
    due_date = models.DateField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
