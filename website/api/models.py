from django.db import models


class MarkdownModel(models.Model):
    """A model to store markdown files"""

    title = models.CharField(max_length=80)
    file = models.FileField(upload_to="markdown/")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"

    # def save(self, *args, **kwargs):
    #     print('saving model somewhere')
    #     print(args, kwargs)
    #     return super().save(*args, **kwargs)


class NotificationModel(models.Model):
    """A model that represents a notification."""

    message = models.TextField()
    source = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        """Return the notification sent."""
        return f"{self.message}"


class DataModel(models.Model):
    """A model that represents data sent by either POST or GET requests."""

    content = models.JSONField()
    source = models.GenericIPAddressField()
    view_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
