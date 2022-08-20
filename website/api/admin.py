from django.contrib import admin
from .models import MarkdownModel, NotificationModel, DataModel

admin.site.register(MarkdownModel)
admin.site.register(NotificationModel)
admin.site.register(DataModel)
