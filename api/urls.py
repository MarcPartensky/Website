from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('random', views.random_req, name='random'),
    path('addition', views.addition, name='addition'),
    path('example', views.ExampleView.as_view(), name='example'),
    path('upload2/', views.FileUploadView.as_view(), name='upload'),
    path('upload/', views.upload_file, name='upload'),
    path('upload-markdown/', views.upload_markdown, name='upload-markdown'),
    # path('user/create/', views.user.create, name="user-create"),
    # path('<str:room_name>/', views.room, name='room'),
]
