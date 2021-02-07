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


class Script(models.Model):
    """Representation of a script."""

    title = models.CharField(max_length=256, unique=True)
    file = models.FileField(upload_to="script/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    read = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return the string representation of the game."""
        return str(self.file)


# class GamePostImageUrl(models.Model):
#     """Representation of a gamepost image url."""
#     url = models.URLField()
#     gamepost = models.ForeignKey(GamePost, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(default=timezone.now)
#     likes = models.PositiveIntegerField(default=0)
#     dislikes = models.PositiveIntegerField(default=0)
#     views = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         """Return the url of the image."""
#         return self.url

# class GamePostComment(models.Model):
#     """Representation of a comment for the game posts.
#     Since a game post could have multiple comments,
#     this uses a many to one relationship pointing to
#     the author of the given comment."""
#     gamepost = models.ForeignKey(GamePost, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.CharField(max_length=1000)
#     timestamp = models.DateTimeField(default=timezone.now)
#     likes = models.PositiveIntegerField(default=0)
#     dislikes = models.PositiveIntegerField(default=0)
#     views = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         """Return the string representation of a comment."""
#         return f"{self.gamepost}-{self.author}:{self.content}"
