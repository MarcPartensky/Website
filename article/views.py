from django.shortcuts import render, HttpResponse, Http404
from .models import ArticleModel
import os

# Create your views here.
def index(request):
    """Select or create an article."""
    context = {
        'articles': []
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
                <link href=\"{% static 'home/assets/img/white-orchid.svg' %}\" rel=\"icon\">\n\
                <link href=\"{% static 'home/assets/img/black-orchid.svg' %}\" rel=\"apple-touch-icon\">"\
                + text
        text = text.replace(
            "<link rel=\"stylesheet\" href=\"assets/css/style.css\" />",
            "<link rel=\"stylesheet\" href=\"{% static 'article/assets/css/style-mixu.css' %}\"/>\n\
            <link rel=\"stylesheet\" href=\"{% static 'article/assets/css/style.css' %}\"/>")
        text = text.replace(
            "<link rel=\"stylesheet\" href=\"assets/css/pilcrow.css\" />",
            "<link rel=\"stylesheet\" href=\"{% static 'article/assets/css/pilcrow.css'%}\"/>")
        text = text.replace(
            "<link type=\"text/css\" rel=\"stylesheet\" href=\"assets/css/hljs-github.min.css\"/>",
            "<link rel=\"stylesheet\" href=\"{% static 'article/assets/css/hljs-github.min.css' %}\"/>")
        f.write(text)

def read(request, title):
    """Read an article."""
    if not f"{title.replace('.md', '')}.md" in os.listdir(f"{os.getcwd()}/media/article"):
        raise Http404("This article was not found.")
    elif title.endswith('.md'):
        with open(f"{os.getcwd()}/media/article/{title}", "r") as f:
            text = str(f.read())
        return HttpResponse(text)
    elif not f"{title}.html" in os.listdir(f"{os.getcwd()}/article/templates/article"):
        print(f'removing {title}.html')
        os.system(f"rm {os.getcwd()}/article/templates/article/{title}.html")
        make(title)
    return render(request, f"article/{title}.html", {})
