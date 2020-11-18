from django.db import models

class ArticleModel(models.Model):
    """A model to store markdown files"""

    title = models.CharField(max_length = 80)
    file = models.FileField(upload_to='article/')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"
