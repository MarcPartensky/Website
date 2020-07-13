from django.urls import path
from . import views

urlpatterns = [
    path('', views.touch_typing, name='touch-typing'),
]