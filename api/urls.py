from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path("random", views.random_req, name="random"),
    path("addition", views.addition, name="addition"),
    path("example", views.ExampleView.as_view(), name="example"),
    path("upload2/", views.FileUploadView.as_view(), name="upload"),
    path("upload/", views.upload_file, name="upload"),
    path("upload-markdown/", views.upload_markdown, name="upload-markdown"),
    path("view-markdown/", views.view_markdown, name="view-markdown"),
    # path('user/create/', views.user.create, name="user-create"),
    # path('<str:room_name>/', views.room, name='room'),
    path("login", views.login, name="api-login"),
    path("python/<str:cmd>", views.python, name="python"),
    path("todo", views.todo_index, name="api-todo-index"),
    path("todo/<str:id>", views.todo, name="api-todo"),
    path("port/<int:n>", views.port, name="port"),
    path("port", views.port, name="port"),
    path("store", views.store, name="store"),
    path("store/<int:id>", views.read_store, name="read-store"),
]
