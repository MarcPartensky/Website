from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.core.exceptions import ViewDoesNotExist


# def response_error_handler(request, exception=None):
# raise HttpResponse('<div class="tenor-gif-embed" data-postid="5094560" data-share-method="host" data-width="100%" data-aspect-ratio="1.7543859649122806"><a href="https://tenor.com/view/elmo-shrug-gif-5094560">Elmo Shrug GIF</a> from <a href="https://tenor.com/search/elmo-gifs">Elmo GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>', status=404)


def not_found_view(request):
    raise ViewDoesNotExist


urlpatterns = [
    path("admin/", admin.site.urls),
    # path('users/login/', auth_views.LoginView.as_view()),
    # path('', include('django.contrib.auth.urls')),
    path("", include("users.urls")),
    path("", include("home.urls")),
    path("", include("todo.urls")),
    path("", include("file.urls")),
    path("", include("shell.urls")),
    path("blog/", include("blog.urls")),
    path("first-site/", include("first_site.urls")),
    path("demo/", include("demo.urls")),
    path("game/", include("game.urls")),
    path("project/", include("project.urls")),
    path("planning/", include("planning.urls")),
    path("touch-typing/", include("touch_typing.urls")),
    path("test/", include("test.urls")),
    path("chat/", include("chat.urls")),
    path("isep/", include("isep.urls")),
    path("gallery/", include("gallery.urls")),
    path("design/", include("design.urls")),
    path("cdn/", include("cdn.urls")),
    path("api/", include("api.urls")),
    path("article/", include("article.urls")),
    path("sql/", include("explorer.urls")),
    path("code/", include("editor.urls")),
    # path('accounts/', include('allauth.urls')),
    path("mdeditor/", include("mdeditor.urls")),
    path("404/", not_found_view, name="404"),
    path("business/", include("business.urls")),
    path("avatar/", include("avatar.urls")),
    path("robots.txt", include("robots.urls")),
    path("", include("url.urls")),  # Last url pattern to put
]

# handler404 = response_error_handler

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
