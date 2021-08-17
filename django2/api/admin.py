# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Task, FileNameModel, kabu_db, predict_output3

admin.site.register(Task)
admin.site.register(FileNameModel)
admin.site.register(kabu_db)
admin.site.register(predict_output3)
