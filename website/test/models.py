from django.db import models
from mdeditor.fields import MDTextField


class TestMDEditor(models.Model):
    """Testing MD Editor.
    https://github.com/pylixm/django-mdeditor
    """

    name = models.CharField(max_length=255)
    content = MDTextField()
