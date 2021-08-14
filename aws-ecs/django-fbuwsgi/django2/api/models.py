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

class predict_output(models.Model):
    predict_date = models.CharField(max_length=50)
    kabu_name = models.CharField(max_length=50)
    kabu_value = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.predict_date

# Create your models here.
