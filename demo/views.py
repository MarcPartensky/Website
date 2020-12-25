from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from home.context import hydrate, base

import requests
import os
import re

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

@xframe_options_exempt
@hydrate(base, debug=True)
def index(request, context={}):
    """List all demos available."""
    # demos = os.listdir(f'{os.getcwd()}/demo/templates/demo')
    # demos = [demo.split('.')[0] for demo in demos]
    # blacklist = ('', 'index', 'portfolio-details')
    # demos = [demo for demo in demos if not demo in blacklist]
    context['title'] = f"Demonstrations of Marc Partensky"
                   # demos=demos)
    return render(request, 'demo/index.html', context)

@xframe_options_exempt
# @hydrate(base)
def pixel_art(request, context={}):
    context = dict(title="Pixel-Art")
    return render(request, 'demo/pixel-art.html', context)

@xframe_options_exempt
# @hydrate(base)
def garage(request, context={}):
    return render(request, 'demo/garage.html', context)

@xframe_options_exempt
@hydrate(base)
def calendar(request, context={}):
    return render(request, 'demo/calendar.html', context)

@xframe_options_exempt
# @hydrate(base)
def google_calendar(request, context={}):
    return render(request, 'demo/google-calendar.html', context)

@xframe_options_exempt
# @hydrate(base)
def html(request, context={}):
    return render(request, 'demo/html.html', context)

@xframe_options_exempt
@hydrate(base)
def qrcode(request, context={}):
    return render(request, 'demo/qrcode.html', context)

@xframe_options_exempt
@hydrate(base)
def discord(request, context={}):
    return render(request, 'demo/discord.html', context)

@xframe_options_exempt
@hydrate(base)
def todolist(request, context={}):
    return render(request, 'demo/todolist.html', context)

@xframe_options_exempt
def orasa_beaute(request):
    return render(request, 'demo/orasa-beaute.html', {})

@xframe_options_exempt
def terminal(request):
    """Browser based terminal."""
    context = dict(cmd="Welcome to this terminal.")
    return render(request, 'demo/terminal.html', context)

def cheat(request, cmd:str):
    """Request manual on cheat api."""
    url = f"https://cheat.sh/{cmd}"
    response = requests.get(url)
    text = response.text
    text = re.sub(r'\[[\d;]*m', '', text)
    text = text.replace('\x1b', '')
    return HttpResponse(text)
