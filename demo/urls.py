from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('pixel-art/', views.pixel_art, name='pixel-art'),
    path('une-blague-pas-marrante-pour-le-garage', views.garage, name="garage"),
    path('calendar/', views.calendar, name="calendar"),
    path('google-calendar/', views.google_calendar, name="google-calendar"),
    path('html', views.html, name='html'),
    path('qrcode', views.qrcode, name='qrcode'),
    path('discord', views.discord, name='discord'),
    path('todolist', views.todolist, name='todolist'),
]
