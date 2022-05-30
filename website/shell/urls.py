"""List all the urls of the shell app."""

from django.urls import path
from . import views

urlpatterns = [
    path("setup", views.setup, name="setup"),
    path("shell", views.shell, name="shell"),
]
