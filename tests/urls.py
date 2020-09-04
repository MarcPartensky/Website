from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name="hello"),
    path('date', views.date, name="date"),
    path('count', views.count, name="count"),
]
