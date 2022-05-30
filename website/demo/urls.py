from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="demo"),
    path("pixel-art", views.pixel_art, name="pixel-art"),
    path("garage", views.garage, name="garage"),
    path("calendar", views.calendar, name="calendar"),
    path("google-calendar", views.google_calendar, name="google-calendar"),
    path("html", views.html, name="html"),
    path("qrcode", views.qrcode, name="qrcode"),
    path("discord", views.discord, name="discord"),
    path("todolist", views.todolist, name="todolist"),
    path("orasa-beaute", views.orasa_beaute, name="orasa-beaute"),
    path("terminal", views.terminal, name="terminal"),
    path("cheat/<str:cmd>", views.cheat, name="cheat"),
]
