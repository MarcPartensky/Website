import time
import os
import glob
import datetime
import requests

from django.shortcuts import render, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from .models import Article
from .forms import ArticleForm
from .adapt import adapt

from django.template.loader import engines
from django.views.decorators.csrf import csrf_exempt

from home.context import home, hydrate
from rich import print


def get_article_context(request):
    """Create the context of the article view."""
    d = home(request)
    objects = Article.objects.filter(public=True)
    if request.user.is_authenticated:
        objects.union(Article.objects.filter(author=request.user))
    d["objects"] = objects
    return d


def reset_template_cache():
    """Attempt to get rid of template caching of django."""
    print("engines:", engines)
    for engine in engines.all():
        print("engine:", engine.engine.template_loaders[0])
        engine.engine.template_loaders[0].reset()


@hydrate(get_article_context)
def index(request, context={}):
    """Select or create an article."""
    return render(request, "article/index.html", context)


def clean_templates():
    """Remove the unused templates."""
    # print(f"{os.getcwd()}/article/static/cache")
    # print('machin directory:', os.listdir(f"{os.getcwd()}/article/static"))
    # print(os.listdir(f"{os.getcwd()}/article/static/cache"))
    # os.system(f"rm -rf {os.getcwd()}/article/templates/article/cache")
    # os.system(f"mkdir {os.getcwd()}/article/templates/article/cache")
    static_cache_path = os.path.join(os.getcwd(), "article/static/article/cache")
    templates_cache_path = os.path.join(os.getcwd(), "article/templates/cache")

    if os.path.exists(static_cache_path):
        os.system(f"rm -rf {static_cache_path}")
    # print("static:", static_cache_path)
    # print("templates:", templates_cache_path)

    if os.path.exists(templates_cache_path):
        print(
            "before deleting templates",
            os.listdir(templates_cache_path),
        )
    path = os.path.join(templates_cache_path, "*")
    # print('path:', path)
    for file in glob.glob(path):
        print(file, "is deleted.")
        os.remove(file)
        print(
            "after deleting templates",
            os.listdir(templates_cache_path),
        )


def build_template(title: str, article: Article, layout: str = "marc"):
    """Build the template and its assets."""
    markdown_path = os.path.join(os.getcwd(), f"media/article/{title}.md")
    html_path = os.path.join(os.getcwd(), f"article/templates/cache/{title}.html")
    article_templates = os.path.join(os.getcwd(), "article/templates/cache")
    article_static = os.path.join(os.getcwd(), "article/static/article")

    with open(markdown_path, "w") as f:
        f.write(article.content)

    cmd = " ".join(
        (
            os.path.join(os.getcwd(), "node_modules/.bin/generate-md"),
            f" --layout {layout}",
            f" --input {markdown_path}",
            f" --output {article_templates}",
        )
    )

    print(cmd)
    os.system(cmd)

    layout_path = os.path.join(article_templates, layout)

    os.rename(os.path.join(article_templates, "assets"), layout_path)

    if layout in os.listdir(article_static):
        os.system(f"rm -rf {layout_path}")
    # else:
    os.system(f"mv {layout_path} {article_static}")

    with open(html_path, "r") as f:
        text = str(f.read())
    text = adapt(text, title, layout)
    with open(html_path, "w") as f:
        f.write(text)


def read(request, title: str):
    """Read an article."""
    reset_template_cache()
    clean_templates()

    title_no_extension = "".join(title.split(".")[:-1])
    print("title no extension:", title_no_extension)

    article = Article.objects.filter(title=title_no_extension).first()
    if not article:
        raise Http404("This article was not found.")

    print("GET:", request.GET)
    layout = request.GET.get("layout") or article.layout or "marc"
    layouts = os.listdir("./node_modules/markdown-styles/layouts")

    article.read = datetime.datetime.now()
    article.view_count += 1
    article.save()

    if layout not in layouts:
        print(layout, "not in ", layouts)
        return render(request, "article/403.html", dict(layouts=layouts))

    if title.endswith(".md"):
        return HttpResponse(article.content, content_type="text/markdown")

    extensions = ["pdf", "docs"]

    for extension in extensions:
        if title.endswith(extension):
            return read_as(article, extension)

    # Never happens since order matters in `urls.py`.
    if title == "index":
        raise PermissionDenied

    build_template(title, article, layout)

    # Messing with template loader cache system
    title_template = title + "." + str(time.time())

    path = os.path.join(os.getcwd(), f"article/templates/cache/{title_template}.html")

    title_path = os.path.join(os.getcwd(), f"article/templates/cache/{title}.html")

    os.system(f"mv {title_path} {path}")

    print(os.listdir(os.path.join(os.getcwd(), f"article/templates/cache/")))

    # Fill context with http parameters and article meta data.
    # Deal with priority when combined dictionaries
    # have the same keys.
    context = dict(stats=os.stat(path))
    context.update(article.__dict__)
    context.update(request.GET)
    return render(request, f"cache/{title_template}.html", context)

    # print(f'removing {title}.html')
    # title_layout = title + "." + layout
    # elif not f"{title}.html" in os.listdir(f"{os.getcwd()}/article/templates/article"):
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


def fetch_article_data(file, request):
    """Read a file to fetch data to fill the sql fields."""
    d = {}
    d["title"] = request.POST.get("title") or str(file)
    if d["title"].endswith(".md"):
        d["title"] = d["title"][:-3]
    print(type(file))
    # d['file'] = file
    d["content"] = file.read().decode("utf-8")
    if request.user:
        d["author"] = request.user
    d["public"] = request.POST.get("public") or False
    print(d)
    return d


def read_as(article: Article, extension: str):
    """Read the markdown as a pdf using the pandoc api."""
    from django_project.settings import PANDOC_API_URL as host

    # Post markdown to pandoc api
    post_url = f"{host}/api/{article.title}.{extension}"
    print("post url:", post_url)
    requests.post(
        post_url,
        files={"file": (article.title, article.content)},
        data={"output": "extension"},
    )

    # Get generated page in pandoc api
    get_url = f"{host}/file/{article.title}.{extension}"
    print("get url:", get_url)
    return HttpResponse(
        requests.get(get_url).content, content_type=f"application/{extension}"
    )

@csrf_exempt
def upload(request):
    """Upload a new article."""
    print("received markdown")
    if request.method == "POST":
        print(request.FILES)
        d = fetch_article_data(request.FILES["file"], request)
        form = ArticleForm(d)
        if form.is_valid():
            print("[lightgreen]valid form[/]")
            form.save()
            return HttpResponse("success")
        print("[red]invalid form[/]")
        print(f"[red]{form.errors.as_data()}[/]")
        return HttpResponse("invalid form", status=500)
    if request.method == "GET":
        form = ArticleForm()
        context = dict(form=form)
        return render(request, "api/upload.html", context)
    raise PermissionDenied("Only GET and POST methods are allowed")
