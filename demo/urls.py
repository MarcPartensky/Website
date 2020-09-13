from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('pixel-art/', views.pixel_art, name='pixel-art'),
    path('une-blague-pas-marrante-pour-le-garage', views.garage, name="garage")
]
