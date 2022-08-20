from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class ProjectPost(models.Model):
    """Representation of a project post."""

    title = models.CharField(max_length=100)
    thumbnail = models.URLField()
    content = models.TextField()
    play = models.URLField()
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return the string representation of the project."""
        return self.title

    def get_absolute_url(self):
        """Return the url of the post."""
        return reverse("project")


class ProjectPostImageUrl(models.Model):
    """Representation of a projectpost image url."""

    url = models.URLField()
    projectpost = models.ForeignKey(ProjectPost, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return the url of the image."""
        return self.url


class ProjectPostComment(models.Model):
    """Representation of a comment for the project posts.
    Since a project post could have multiple comments,
    this uses a many to one relationship pointing to
    the author of the given comment."""

    projectpost = models.ForeignKey(ProjectPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return the string representation of a comment."""
        return f"{self.projectpost}-{self.author}:{self.content}"
