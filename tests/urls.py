from django.urls import path, re_path
from . import views

urlpatterns = [
    path('hello', views.hello, name="hello"),
    path('date', views.date, name="date"),
    path('count', views.count, name="count"),
    path('url', views.url, name="url"),
    path('args/(?.*)', views.url, name='args'),
    re_path('addition/?(d/)*', views.addition, name='addition'),
    path('user-agent', views.user_agent, name="user-agent"),
    path('homepage1', views.homepage1, name="homepage1"),
    path('vanta-net', views.vanta_net, name="vanta-net"),
    path('programming-languages-logo', views.programming_languages_logo,
         name="programming-languages-logo"),
    path('ace-editor', views.ace_editor, name="ace-editor"),
    path('codemirror-editor', views.codemirror_editor, name="codemirror-editor"),
]
