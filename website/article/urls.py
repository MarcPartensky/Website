from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="article"),
    path("upload", views.upload, name="article-upload"),
    path("<str:title>", views.read, name="article-read"),
]
