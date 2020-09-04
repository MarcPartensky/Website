from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name="about"),
    path('donation', views.donation, name="donation"),
    path('cv', views.cv, name="cv"),
    path('contact', views.contact, name="contact"),
]

