from django.contrib import admin

from . import models

admin.site.register(models.File)
admin.site.register(models.Access)
admin.site.register(models.Permission)
admin.site.register(models.Token)
