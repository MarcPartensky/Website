"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.core.exceptions import ViewDoesNotExist 

def response_error_handler(request, exception=None):
    raise HttpResponse('<div class="tenor-gif-embed" data-postid="5094560" data-share-method="host" data-width="100%" data-aspect-ratio="1.7543859649122806"><a href="https://tenor.com/view/elmo-shrug-gif-5094560">Elmo Shrug GIF</a> from <a href="https://tenor.com/search/elmo-gifs">Elmo GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>', status=404)


def not_found_view(request):
    raise ViewDoesNotExist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('blog/', include('blog.urls')),
    path('first-site/', include('first_site.urls')),
    path('', include('home.urls')),
    path('demo/', include('demo.urls')),
    path('games/', include('games.urls')),
    path('projects/', include('projects.urls')),
    path('planning/', include('planning.urls')),
    path('touch-typing/', include('touch_typing.urls')),
    path('tests/', include('tests.urls')),
    path('chat/', include('chat.urls')),
    path('isep/', include('isep.urls')),
    path('404/', ViewDoesNotExist),
]

handler404 = response_error_handler


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
