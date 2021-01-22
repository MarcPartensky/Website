from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.todo, name='todo'),
    path('todo-state', views.todo_state, name='todo-state'),
    path('todo-done', views.todo_done, name='todo-done'),
    path('todo-new', views.todo_new, name='todo-new'),
    path('todo/:id/update', views.todo_update, name='todo-update'),
    path('todo/:id/delete', views.todo_delete, name='todo-delete'),
]
