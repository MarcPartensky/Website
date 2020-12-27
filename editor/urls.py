from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='code'),
    path('script', views.script_index, name="code-script-index"),
    path('script/<str:title>', views.script, name="code-script"),
    # path('account/', views.account, name="account"),
    # path()
    path('<str:user>', views.user_index, name="code-user"),
    path('<str:user>/<str:project>',
         views.project, name="code-user-project"),
    path('<str:user>/<str:project>/<str:filepath>',
         views.file, name="code-user-project-filepath"),
]

