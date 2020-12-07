from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='code'),
    path('<str:id>', views.project, name="project"),
]

