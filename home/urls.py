from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("donation", views.donation, name="donation"),
    path("cv", views.cv, name="cv"),
    path("cv/1p", views.cv_1p, name="cv-1p"),
    path("cv/2p", views.cv, name="cv-2p"),
    path("contact", views.contact, name="contact"),
    path("resume", views.resume, name="resume"),
    path("notified-mail-form", views.notified_mail_form, name="notified-mail-form"),
    path("notified-mail-list", views.notified_mail_list, name="notified-mail-list"),
    re_path(r"^db_graph\.([a-z]*)", views.db_graph, name="db-graph"),
]

# from django.conf.urls import (
# handler400, handler403, handler404, handler500
# )

# handler400 = 'home.views.bad_request'
# handler403 = 'home.views.permission_denied'
# handler404 = 'home.views.page_not_found'
# handler500 = 'home.views.server_error'
