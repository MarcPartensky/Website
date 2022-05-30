from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class File(models.Model):
    """Representation of a file."""

    title = models.CharField(max_length=256)
    file = models.FileField(upload_to="script/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    read = models.DateTimeField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return the string representation of the game."""
        return str(self.file)


class Script(File):
    """Representation of a script."""

    ran = models.PositiveIntegerField(default=0)

    def update(self):
        """Cout how many times this script was run."""
        pass
