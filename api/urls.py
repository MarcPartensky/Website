from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('random', views.random_req, name='random'),
    path('addition', views.addition, name='addition'),
    path('example', views.example , name='example'),
    # path('user/create/', views.user.create, name="user-create"),
    # path('<str:room_name>/', views.room, name='room'),
]
