from django.db import models

# Create your models here.

class NotifiedMailList(models.Model):
    """Notify all users from that list
    when an event pops out."""
    email = models.EmailField()
