from django.urls import path, re_path
from markdown_view.views import MarkdownView
from . import views

urlpatterns = [
    path("hello", views.hello, name="hello"),
    path("date", views.date, name="date"),
    path("count", views.count, name="count"),
    path("url", views.url, name="url"),
    path("args/(?.*)", views.url, name="args"),
    re_path("addition-1/?(d/)*", views.addition1, name="addition"),
    re_path("addition-2", views.addition2, name="addition"),
    path("user-agent", views.user_agent, name="user-agent"),
    path("homepage1", views.homepage1, name="homepage1"),
    path("vanta-net", views.vanta_net, name="vanta-net"),
    path(
        "programming-languages-logo",
        views.programming_languages_logo,
        name="programming-languages-logo",
    ),
    path("ace-editor", views.ace_editor, name="ace-editor"),
    path("codemirror-editor", views.codemirror_editor, name="codemirror-editor"),
    path("xterm", views.xterm, name="xterm"),
    path("skulpt", views.skulpt, name="skulpt"),
    path(
        "codemirror+skulpt", views.codemirror_plus_skulpt, name="codemirror_plus_skulpt"
    ),
    path(
        "todolist2",
        MarkdownView.as_view(file_name="test/templates/test/todolist.md"),
        name="todolist2",
    ),
    path("todolist", views.todolist, name="todolist"),
    path("discordbot", views.discordbot, name="discordbot"),
    path("websocket", views.websocket, name="websocket"),
    path("valentin", views.valentin, name="valentin"),
    path("paul", views.paul, name="paul"),
    # path('mdeditor', views.mdeditor, name='mdeditor'),
]
