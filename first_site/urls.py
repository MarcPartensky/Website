from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='first-site'),
    path('circles/',views.circle,name="circles"),
    path('geometry/',views.geometry,name="geometry"),
    path('intersection/',views.intersection,name="intersection"),
    path('physics/',views.physics,name="physics"),
    path('asteroids/',views.asteroids,name="asteroids"),
    path('cube/',views.cube,name="cube"),
    path('connect4/',views.connect4,name="connect4"),
    path('expanse/',views.expanse,name="expanse"),
]