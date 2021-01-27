from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    """A model to store markdown files"""

    title = models.CharField(max_length=255, unique=True)
    # file = models.FileField(upload_to='article/')
    content = models.TextField(null=True)

    author = models.OneToOneField(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    public = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    read = models.DateTimeField(null=True)
    # uuid = models.UUIDField(editable=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        """Return the title of the article."""
        return f"{self.title}"

    # @property
    # def preview(self, n=500):
    #     """"""

# class WritersGroup
# article = models.ForeignKey(ArticleModel)
