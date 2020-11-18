from django.shortcuts import render, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from .models import ArticleModel
import os

# Create your views here.
def index(request):
    """Select or create an article."""
    titles = os.listdir(f"{os.getcwd()}/media/article")
    class Article:
        def __init__(self, title):
            self.title = title.replace('.md', '')
            with open(f"{os.getcwd()}/media/article/{title}", "r") as f:
                self.preview = str(f.read())[:500].replace('\n', '<br>')

    articles = []
    for title in titles:
        articles.append(Article(title))


    context = {
        'articles': articles
    }
    return render(request, 'article/index.html', context)

def make(title):
    os.system(f"generate-md --layout mixu-radar \
              --input {os.getcwd()}/media/article/{title}.md \
              --output {os.getcwd()}/article/templates/article")
    os.system(f"rm -rf {os.getcwd()}/article/templates/article/assets")
    with open(f"{os.getcwd()}/article/templates/article/{title}.html", "r") as f:
        text = str(f.read())
    with open(f"{os.getcwd()}/article/templates/article/{title}.html", "w") as f:
        # text = "{% extends \"layout/home.html\" %} \
        #         {% load static %} \
        #         {% block content %}" + text + "{% endblock content %}"
        text = "{% load static %}\n\
        <script src=\"{% static 'home/assets/vendor/jquery/jquery.min.js'%}\"></script>\n\
        <link href=\"{% static 'home/assets/img/white-orchid.svg' %}\" rel=\"icon\">\n\
        <link href=\"{% static 'home/assets/img/black-orchid.svg' %}\" rel=\"apple-touch-icon\">"\
        + text
        text = text.replace(
            "<link rel=\"stylesheet\" href=\"assets/css/style.css\" />",
            "<link rel=\"stylesheet\" href=\"{% static 'article/assets/css/style-mixu.css' %}\"/>\n\
            <link rel=\"stylesheet\" href=\"{% static 'article/assets/css/style.css' %}\"/>")
            # <link rel=\"stylesheet\" href=\"{% static 'article/assets/css/copy-pre.css' %}\"/>\
            # <script src=\"{% static 'article/assets/js/copy-pre.js' %}\"><script>")
        text = text.replace(
            "<link rel=\"stylesheet\" href=\"assets/css/pilcrow.css\" />",
            "<link rel=\"stylesheet\" href=\"{% static 'article/assets/css/pilcrow.css'%}\"/>")
        text = text.replace(
            "<link type=\"text/css\" rel=\"stylesheet\" href=\"assets/css/hljs-github.min.css\"/>",
            "<link rel=\"stylesheet\" href=\"{% static 'article/assets/css/hljs-github.min.css' %}\"/>")
        text = text.replace("</body>", "\
        <script src=\"{% static 'home/assets/vendor/waypoints/jquery.waypoints.min.js' %}\"></script>\n\
        <script src=\"{% static 'article/assets/js/main.js' %}\"></script>\n\
        </body>")
        f.write(text)

def read(request, title):
    """Read an article."""
    if not f"{title.replace('.md', '')}.md" in os.listdir(f"{os.getcwd()}/media/article"):
        raise Http404("This article was not found.")
    elif title.endswith('.md'):
        with open(f"{os.getcwd()}/media/article/{title}", "r") as f:
            text = str(f.read())
        return HttpResponse(text)
    # elif not f"{title}.html" in os.listdir(f"{os.getcwd()}/article/templates/article"):
    if title == "index":
        raise PermissionDenied
    print(f'removing {title}.html')
    os.system(f"rm {os.getcwd()}/article/templates/article/{title}.html")
    make(title)
    return render(request, f"article/{title}.html", {})
