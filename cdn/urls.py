from django.urls import path
from . import views

urlpatterns = [
    path('cdn.js', views.cdn, name='cdn'),
    path('test.html', views.test, name='test'),
]

