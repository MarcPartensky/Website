"""Coding app so that I can code anywhere."""

from django.shortcuts import render
from home.context import hydrate, home

@hydrate(home)
def index(request, context: dict = {}):
    """Render all code projects."""
    return render(request, 'editor/index.html', context)

def script(request, context: dict = {}):
    """Render a script."""
    return render(request, 'editor/script.html', context)

def user(request, user: str, context: dict = {}):
    """Render a user."""
    return render(request, 'editor/user.html', context)

def project(request,
            user: str,
            project: str,
            context: dict = {}):
    """Render a code project."""
    return render(request, 'editor/project.html', context)

def file(request,
         user: str,
         project: str,
         filepath: str,
         context: dict = {}):
    """Render a file."""
    return render(request, 'editor/file.html', context)

