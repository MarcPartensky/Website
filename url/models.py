from django.db import models


class Url(models.Model):
    """Url representation for redirection."""

    url = models.URLField()
    title = models.CharField()
    description = models.TextField()

    def __str__(self):
        """Return the title of the url model."""
        return self.title
