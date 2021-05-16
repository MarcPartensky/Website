from django.urls import path
from . import views

urlpatterns = [
    path("u<str:id>", views.url, name="url"),
    path("urls", views.urls, name="urls"),
]
