from django.urls import path
from . import views

urlpatterns = [
    path('', views.isep, name="isep"),
    path('app/', views.app, name="app"),
    path('planning-app/', views.planning_app, name="planning-app"),
    path('lignee', views.lignee, name="lignee"),
]
