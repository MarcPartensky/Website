from django.urls import path
from . import views

urlpatterns = [
    # default file access
    path("file", views.index, name="file-index"),
    path("file/<str:id>", views.file, name="file"),
    # short file access
    path("f", views.access_index, name="file-access-index"),
    path("f/<str:uuid>", views.access, name="file-access"),
]
