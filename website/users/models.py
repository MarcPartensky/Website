from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import JSONField

# from . import article
from article.models import ArticleLayout

from PIL import Image


# class Theme(models.IntegerChoices):
#     """Website theme."""
#     LIGHT = 1
#     DARK = 2


class Preference(models.Model):
    """Representation of a preference."""

    # data = models.JSONField(blank=True, null=True)
    data = JSONField(blank=True, null=True)
    article_layout = models.CharField(
        max_length=255,
        choices=ArticleLayout.choices,
        null=True,
    )
    # article_layout = models.OneToOneField(
    #     ArticleLayout,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True)
    # theme = models.PositiveSmallIntegerField(choices=)
    theme = models.IntegerChoices("Theme", "LIGHT DARK")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the string representation of a preference."""
        # return f'{self.}''
        return super().__str__()


class Profile(models.Model):
    """Representation of a user profile."""
    default_avatar = "media/assets/img/default_avatar.svg",

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    preference = models.ForeignKey(to=Preference, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the string representation of a string."""
        return self.user.username

    def get_avatar(self):
        """Return an avatar."""
        return self.image or Profile.default_avatar

"""
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        width,height = img.size
        if width > 300 or height > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
"""
