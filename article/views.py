from django.shortcuts import render, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.template import loader
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
    # print(f"{os.getcwd()}/article/static/cache")
    # print('machin directory:', os.listdir(f"{os.getcwd()}/article/static"))
    # print(os.listdir(f"{os.getcwd()}/article/static/cache"))
    os.system(f"rm -rf {os.getcwd()}/article/static/article/cache")
    # os.system(f"rm -rf {os.getcwd()}/article/templates/article/cache")
    # os.system(f"mkdir {os.getcwd()}/article/templates/article/cache")
    print('before deleting templates', os.listdir(f"{os.getcwd()}/article/templates/cache"))
    for file in glob.glob(f"{os.getcwd()}/article/templates/cache/*"):
        print(file, 'is deleted.')
        os.remove(file)
        print('after deleting templates', os.listdir(f"{os.getcwd()}/article/templates/cache"))

def make(title:str, layout:str="marc"):
    os.system(f"{os.getcwd()}/node_modules/.bin/generate-md --layout {layout}\
              --input {os.getcwd()}/media/article/{title}.md \
              --output {os.getcwd()}/article/templates/cache")
    os.rename(f"{os.getcwd()}/article/templates/cache/assets",
              f"{os.getcwd()}/article/templates/cache/{layout}")
    if layout in os.listdir(f"{os.getcwd()}/article/static/article/"):
        os.system(f"rm -rf {os.getcwd()}/article/templates/cache/{layout}")
    else:
        os.system(f"mv {os.getcwd()}/article/templates/cache/{layout}\
                  {os.getcwd()}/article/static/article")
    with open(f"{os.getcwd()}/article/templates/cache/{title}.html", "r") as f:
        text = str(f.read())
    # text = text.replace('&&title&&', title.capitalize())
    text = adapt(text, title, layout)
    with open(f"{os.getcwd()}/article/templates/cache/{title}.html", "w") as f:
        f.write(text)

def read(request, title:str):
    """Read an article."""
    clean()
    print(request.GET)
    if 'layout' in request.GET:
        layout = request.GET['layout']
    else:
        layout = "marc"
    layouts = os.listdir("./node_modules/markdown-styles/layouts")
    if layout not in layouts:
        print(layout, 'not in ', layouts)
        return render(request, 'article/403.html', dict(layouts=layouts))
    elif not f"{title.replace('.md', '')}.md" in os.listdir(f"{os.getcwd()}/media/article"):
        print(title, 'not in', os.listdir(f"{os.getcwd()}/media/article"))
        raise Http404("This article was not found.")
    elif title.endswith('.md'):
        with open(f"{os.getcwd()}/media/article/{title}", "r") as f:
            text = str(f.read())
        return HttpResponse(text)
    # elif not f"{title}.html" in os.listdir(f"{os.getcwd()}/article/templates/article"):
    elif title == "index":
        print("index is reserved")
        raise PermissionDenied
    #print(f'removing {title}.html')
    title_layout = title + "." + layout
    make(title, layout)
    os.system(f"mv \
        {os.getcwd()}/article/templates/cache/{title}.html \
        {os.getcwd()}/article/templates/cache/{title_layout}.html"
    )
    print(os.listdir(f"{os.getcwd()}/article/templates/cache/"))
    return render(request, f"cache/{title_layout}.html", request.GET)

    # return render(request, f"cache/{title}.html", request.GET)
    # context = dict(**request.GET)
    # print(context)
    # template = loader.get_template(f"cache/{title_layout}.html")
    # os.system(f'head -n 20 {os.getcwd()}/article/templates/cache/{title_layout}.html')
    # html = template.render(context, request)
    # # template.render()
    # # template.render(clean=True)
    # print(html[:1000])
    # print("code generated")
    # return HttpResponse(html)
