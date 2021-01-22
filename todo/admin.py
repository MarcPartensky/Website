from django.contrib import admin
from . import models


admin.site.register(models.TodoState)
admin.site.register(models.TodolistState)
admin.site.register(models.Todo)
admin.site.register(models.Todolist)
