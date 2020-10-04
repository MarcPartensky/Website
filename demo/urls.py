from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('pixel-art/', views.pixel_art, name='pixel-art'),
    path('une-blague-pas-marrante-pour-le-garage', views.garage, name="garage"),
    path('google-calendar/', views.google_calendar, name="google-calendar"),
    path('google-official-calendar/', views.google_official_calendar, name="google-official-calendar"),
    path('html/', views.html, name='html'),
    path('qrcode/', views.qrcode, name='qrcode'),
]
