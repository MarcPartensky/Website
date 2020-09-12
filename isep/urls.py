from django.urls import path
from . import views

urlpatterns = [
    path('', views.isep, name="isep"),
    path('app', views.app, name="app"),
]
