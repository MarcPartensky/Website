from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import uuid

# class ArticleLayout(models.Model):
#     """A model that stores possible article layouts."""
#     name = models.CharField(max_length=255)
#     author = models.OneToOneField(
#         User, on_delete=models.SET_NULL, blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         """Return the name of the article layout."""
#         return f"{self.name}"

class ArticleLayout(models.TextChoices):
    BOOTSTRAP3 = 'bootstrap3'
    GITHUB = 'github'
    JASONM23_DARK = 'jasonm23-dark'
    JASONM23_FOGHORN = 'jasonm23-foghorn'
    JASONM23_MARKDOWN = 'jasonm23-markdown'
    JASONM23_SWISS = 'jasonm23-swiss'
    MARC = 'marc'
    MARKEDAPP_BYWORD = 'markedapp-byword'
    MIXU_BOOK = 'mixu-book'
    MIXU_BOOTSTRAP_2COL = 'mixu_bootstrap-2col'
    MIXU_BOOTSTRAP = 'mixu-bootstrap'
    MIXU_GRAY = 'mixu-gray'
    MIXU_PAGE = 'mixu-page'
    MIXU_RADAR = 'mixu-radar'
    RORYG_GHOSTWRITER = 'roryg_ghostwriter'
    THOMASF_SOLARIZEDCSSDARK = 'thomasf_solarizedcssdark'
    THOMASF_SOLARIZEDCSSLIGHT = 'thomasf_solarizedcsslight'


class Article(models.Model):
    """A model to store markdown files."""
    title = models.CharField(max_length=255, unique=True)
    # file = models.FileField(upload_to='article/')
    content = models.TextField(null=True)

    author = models.OneToOneField(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    public = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    update_count = models.PositiveIntegerField(default=0) # version
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    read = models.DateTimeField(null=True)
    layout = models.CharField(
        max_length=255,
        choices=ArticleLayout.choices,
        default=ArticleLayout.MARC)
    # Unique way to identify an article which never changes
    # uuid = models.UUIDField(
    #     editable=False, unique=True, default=uuid.uuid4)

    class Meta:
        ordering = ['title']

    def __str__(self):
        """Return the title of the article."""
        return f"{self.title}"

    def update_article(self):
        """Update the article fields for new version."""
        self.update_count += 1
        self.updated = timezone.now()

    def update_view(self):
        """Update the article fields for new view."""
        self.view_count += 1
        self.read = timezone.now()

    # @property
    # def preview(self, n=500):
    #     """"""

# class WritersGroup
# article = models.ForeignKey(ArticleModel)
