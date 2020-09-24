from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name="about"),
    path('donation', views.donation, name="donation"),
    path('cv', views.cv, name="cv"),
    path('contact', views.contact, name="contact"),
]

from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

handler400 = 'home.views.bad_request'
handler403 = 'home.views.permission_denied'
handler404 = 'home.views.page_not_found'
handler500 = 'home.views.server_error'
