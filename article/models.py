from django.db import models
from django.utils import timezone
from users.models import Profile

class ArticleModel(models.Model):
    """A model to store markdown files"""

    title = models.CharField(max_length = 80)
    file = models.FileField(upload_to='article/')

    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True,
                               null=True)
    view_count = models.IntegerField()
    like_count = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    read_date = models.DateTimeField(blank=True)
    public = models.BooleanField(default=True)
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"

# class WritersGroup
# article = models.ForeignKey(ArticleModel)
