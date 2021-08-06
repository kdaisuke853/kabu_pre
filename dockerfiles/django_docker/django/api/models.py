from django.db import models
from datetime import datetime


class Task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FileNameModel(models.Model):
    file_name = models.CharField(max_length=50)
    upload_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.file_name


class kabu_db(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
