from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="business"),
    path("<str:lang>", views.index, name="business"),
    path("offers", views.offers, name="offers"),
]
