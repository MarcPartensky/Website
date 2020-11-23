from django.shortcuts import render, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from .models import ArticleModel
import os
import glob
import random
from .adapt import adapt

class Article:
    @classmethod
    def create(cls, title):
        """Create an article given its title."""
        print(title)
        with open(f"{os.getcwd()}/media/article/{title}", "r") as f:
            preview = str(f.read())[:496]+" ..."
        title = title.replace('.md', '')
        return cls(title, preview)

    def __init__(self, title, preview, active=False):
        "Create an article given its title and preview."
        self.title = title
        self.preview = preview
        self.active = active

# Create your views here.
def index(request):
    """Select or create an article."""
    titles = os.listdir(f"{os.getcwd()}/media/article")
    articles = [Article.create(title) for title in titles if title!='.DS_Store']
    article = random.choice(articles)
    article.active = True
    context = dict(articles=articles)
    return render(request, 'article/index.html', context)


def old_make(title):
    os.system(f"generate-md --layout mixu-radar \
              --input {os.getcwd()}/media/article/{title}.md \
              --output {os.getcwd()}/article/templates/cache")
    os.system(f"rm -rf {os.getcwd()}/article/templates/cache/assets")
    with open(f"{os.getcwd()}/article/templates/cache/{title}.html", "r") as f:
        text = str(f.read())
    with open(f"{os.getcwd()}/article/templates/cache/{title}.html", "w") as f:
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
        pattern = re.compile(r'<title>(.*)</title>')
        wrong_title = re.findall(pattern, text)[0]
        text = text.replace(f"<title>{wrong_title}</title>",
                            f"<title>{title.capitalize()}</title>")
        f.write(text)

def clean():
    os.system(f"rm -rf {os.getcwd()}/article/static/article/cache")
    for file in glob.glob(f"{os.getcwd()}/article/templates/cache/*"):
        os.remove(file)

def make(title:str, layout:str="marc"):
    os.system(f"{os.getcwd()}/node_modules/.bin/generate-md --layout {layout}\
              --input {os.getcwd()}/media/article/{title}.md \
              --output {os.getcwd()}/article/templates/cache")
    os.rename(f"{os.getcwd()}/article/templates/cache/assets",
              f"{os.getcwd()}/article/templates/cache/cache")
    os.system(f"mv {os.getcwd()}/article/templates/cache/cache\
              {os.getcwd()}/article/static/article")
    with open(f"{os.getcwd()}/article/templates/cache/{title}.html", "r") as f:
        text = str(f.read())
    # text = text.replace('&&title&&', title.capitalize())
    text = adapt(text, title)
    with open(f"{os.getcwd()}/article/templates/cache/{title}.html", "w") as f:
        f.write(text)

def read(request, title):
    """Read an article."""
    clean()
    if 'layout' in request.GET:
        layout = request.GET['layout']
    else:
        layout = "marc"
    layouts = os.listdir("./node_modules/markdown-styles/layouts")
    if layout not in layouts:
    #     str_layouts = '\n'.join(map(lambda l: f"- {l}", layouts))
    #     text = f"Unauthorized layouts. Your must choose between: \n{str_layouts}"
        # return HttpResponse(text, status=403)
        return render(request, 'article/403.html', dict(layouts=layouts))
    if not f"{title.replace('.md', '')}.md" in os.listdir(f"{os.getcwd()}/media/article"):
        raise Http404("This article was not found.")
    elif title.endswith('.md'):
        with open(f"{os.getcwd()}/media/article/{title}", "r") as f:
            text = str(f.read())
        return HttpResponse(text)
    # elif not f"{title}.html" in os.listdir(f"{os.getcwd()}/article/templates/article"):
    if title == "index":
        raise PermissionDenied
    #print(f'removing {title}.html')
    #os.system(f"rm {os.getcwd()}/article/templates/article/{title}.html")
    # make(title)
    make(title, layout)
    return render(request, f"cache/{title}.html", {})
