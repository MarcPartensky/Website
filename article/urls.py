from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='article'),
    path('<str:title>', views.read , name='article-read'),
]
