from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='code'),
    path('script/', views.script, name="script"),
    path('script/<str:script>', views.script, name="script"),
    # path('account/', views.account, name="account"),
    path('<str:user>', views.user, name="user"),
    path('<str:user>/<str:project>',
         views.project, name="user-project"),
    path('<str:user>/<str:project>/<str:filepath>',
         views.file, name="user-project-filepath"),
]

