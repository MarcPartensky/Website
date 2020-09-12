from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Conversation(models.Model):
    """Representation of a conversation."""
    title = models.CharField(max_length=100)
    thumbnail = models.URLField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return the title of the conversation."""
        return self.title

class Message(models.Model):
    """Representation of a message."""
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return the content of the message."""
        return self.content
