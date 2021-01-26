from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    """A model to store markdown files"""

    title = models.CharField(max_length=80)
    file = models.FileField(upload_to='article/')

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    read = models.DateTimeField(blank=True)
    public = models.BooleanField(default=False)
    description = models.TextField(null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        """Return the title of the article."""
        return f"{self.title}"

    @property
    def markdown(self):
        """Return the markdown representation of the article."""
        with open(self.file, 'r') as f:
            text = f.read()
        return text

# class WritersGroup
# article = models.ForeignKey(ArticleModel)
