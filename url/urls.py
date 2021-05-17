from django.urls import path
from . import views

urlpatterns = [
    path("urls", views.urls, name="urls"),
    path("u", views.url, name="url-simple"),
    path("u<str:route>", views.url, name="url"),
]
