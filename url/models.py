"""Url model."""

import shortuuid

from django.db import models
from shortuuidfield import ShortUUIDField
from django.contrib.auth.models import User
from django.utils import timezone

URL_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~"


def get_uuid():
    """Return a url friendly shortuuid"""
    return shortuuid.ShortUUID(alphabet=URL_ALPHABET).random(6)


class Url(models.Model):
    """Url representation for redirecton."""

    route = ShortUUIDField(
        editable=True,
        default=get_uuid,
        max_length=6,
        unique=True,
    )
    target = models.URLField()
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        """Return the title of the url model."""
        return self.route + " -> " + self.target


class Request(models.Model):
    """Request of url."""

    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
