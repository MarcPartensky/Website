"""Coding app so that I can code anywhere."""

import requests

from django.shortcuts import render
from . import models
from home.context import hydrate
from home.context import fake_base as base
from django.contrib.auth.decorators import login_required, PermissionDenied
from django.http.response import HttpResponse

print(base.__doc__)


class OnlyGetAndPost(PermissionDenied):
    """Exception retured when requesting a view only compatible with GET and
    POST methods."""

    def __str__(self):
        return f"{super().__str__()}: Only get and post exceptions are supported."


@hydrate(base)
def index(request, context: dict = {}):
    """Render all code projects."""
    return render(request, "editor/index.html", context)


@hydrate(base)
def script_index(request, context: dict = {}):
    """Render a list of scripts."""
    scripts = models.Script.objects.all()
    context["scripts"] = scripts
    return render(request, "editor/script_index.html", context)


@login_required
@hydrate(base)
def script(request, title: str, context: dict = {}):
    """Render a script."""
    if request.method == "GET":
        script = models.Script.objects.filter(title=title).first()
        # Use the script found.
        if not script:
            # or create a new script if one does not exist.
            script = models.Script(title=title, author=request.user)
            script.save()
        context["script"] = script
        return render(request, "editor/script.html", context)
    elif request.method == "POST":
        print(f"attempting to post {title}")
        for (k, v) in request.POST.items():
            print(k, "=", v)
        # print(request.)
        pass
    else:
        raise OnlyGetAndPost


@hydrate(base)
def user(request, user: str, context: dict = {}):
    """Render a user."""
    return render(request, "editor/user.html", context)


@hydrate(base)
def user_index(request, context: dict = {}):
    """Render a list of developers."""
    return render(request, "editor/user_index.html", context)


def project(request, user: str, project: str, context: dict = {}):
    """Render a code project."""
    return render(request, "editor/project.html", context)


@hydrate(base)
def file(request, user: str, project: str, filepath: str, context: dict = {}):
    """Render a file."""
    return render(request, "editor/file.html", context)


def github_shell(request, script: str):
    """Finds shell script on github and makes it available from website."""
    url = f"https://raw.githubusercontent.com/MarcPartensky/Shell/master/{script}"
    return HttpResponse(requests.get(url))
