from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class GamePost(models.Model):
    """Representation of a game post."""
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
        """Return the string representation of the game."""
        return self.title

class GamePostImageUrl(models.Model):
    """RepresentatiGamon of a gamepost image url."""
    url = models.URLField()
    gamepost = models.ForeignKey(GamePost, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return the url of the image."""
        return self.url

class GamePostComment(models.Model):
    """Representation of a comment for the game posts.
    Since a game post could have multiple comments,
    this uses a many to one relationship pointing to
    the author of the given comment."""
    gamepost = models.ForeignKey(GamePost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)


    def __str__(self):
        """Return the string representation of a comment."""
        return f"{self.gamepost}-{self.author}:{self.content}"
