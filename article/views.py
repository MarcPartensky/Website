import time
import os
import glob
import random

from django.shortcuts import render, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.template import loader
from .models import Article
from .adapt import adapt

from django.template.loader import engines
from django.views.decorators.csrf import csrf_exempt

from home.context import home, hydrate
from .context import get_articles_objects

def get_article_context(request):
    """Create the context of the article view."""
    d = home(request)
    d.update(get_articles_objects())
    return d

def reset_template_cache():
    """Attempt to get rid of template caching of django."""
    print("engines:", engines)
    for engine in engines.all():
        print('engine:', engine.engine.template_loaders[0])
        engine.engine.template_loaders[0].reset()

@hydrate(get_article_context)
def index(request, context={}):
    """Select or create an article."""
    return render(request, 'article/index.html', context)

def clean():
    """Remove the unused templates."""
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

def make(title: str, layout: str = "marc"):
    """Build the template and its assets."""
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

def read(request, title: str):
    """Read an article."""
    reset_template_cache()
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
        return HttpResponse(text, content_type="text/markdown")
    elif title == "index":
        print("index is reserved")
        raise PermissionDenied
    # Messing with template loader cache system
    title_template = title + "." + str(time.time())
    make(title, layout)
    path = f"{os.getcwd()}/article/templates/cache/{title_template}.html"
    os.system(f"mv \
        {os.getcwd()}/article/templates/cache/{title}.html \
        {path}"
    )
    print(os.listdir(f"{os.getcwd()}/article/templates/cache/"))
    # Fill context with http parameters and article meta data.
    context = dict(**request.GET, stats=os.stat(path))
    return render(request, f"cache/{title_template}.html", context)

    #print(f'removing {title}.html')
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

@csrf_exempt
def upload_article(request):
    """Upload a new article."""
    print('received markdown')
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        file = str(form.files['file'])
        filepath = f"{os.getcwd()}/media/article/{file}"
        print('trying to post:', filepath)
        content = form.files['file'].file.read().decode('utf-8')
        lines = content.split('\n')
        if lines[0].startswith('#!'):
            lines = lines[1:]
        content = '\n'.join(lines).strip()
        with open(filepath, 'w') as f:
            f.write(content)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('invalid form')
    elif request.method == 'GET':
        form = ArticleForm()
        context = dict(form=form)
        return render(request, 'api/upload.html', context)
    else:
        return HttpResponse('only get and post methods are allowed')
