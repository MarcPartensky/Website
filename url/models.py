"""Url model."""

import shortuuid

from django.db import models
from shortuuidfield import ShortUUIDField
from django.contrib.auth.models import User

URL_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~"


def get_uuid():
    """Return a url friendly shortuuid"""
    return shortuuid.ShortUUID(alphabet=URL_ALPHABET).random(6)


class Url(models.Model):
    """Url representation for redirection."""

    route = ShortUUIDField(editable=True, default=get_uuid, max_length=6, unique=True)
    target = models.URLField()
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return the title of the url model."""
        return self.route + " -> " + self.target
