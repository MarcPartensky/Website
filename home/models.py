from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class NotifiedMailList(models.Model):
    """Notify all users from that list
    when an event pops out."""

    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)


# class Theme(models.Model):
#     """Possible theme of the website."""
#     name = models.Choices()
