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
