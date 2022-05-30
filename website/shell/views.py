"""Run a shell scripts on demand."""

import os
import requests

from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from rich import print


def setup(request: HttpRequest):
    """Install all my dependencies based on shell script of my git projects."""
    git_project_shell = os.environ["GIT_PROJECT_SHELL"]
    return HttpResponse("test")


def shell(request: HttpRequest, script: str):
    """Run a shell script bsed on the git shell project environment
    variable."""
    git_project_shell = os.environ["GIT_PROJECT_SHELL"]
    content = requests.get(f"{git_project_shell}/")
    return HttpResponse(content)
