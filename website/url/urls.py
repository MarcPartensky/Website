from django.urls import path
from . import views

urlpatterns = [
    path("urls", views.urls, name="urls"),
    path("requests", views.requests, name="requests"),
    path("u", views.url, name="url-simple-u"),
    path("/", views.url, name="url-simple-slash"),
    path("/<str:route>", views.url, name="url-slash"),
    path("u<str:route>", views.url, name="url"),
]
