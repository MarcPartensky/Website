from django.urls import path
from . import views

urlpatterns = [
    path("", views.design, name="design"),
    path("test-1", views.test_1, name="test-1"),
]
