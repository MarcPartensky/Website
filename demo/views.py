from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

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
def index(request):
    demos = os.listdir(f'{os.getcwd()}/demo/templates/demo')
    demos = [demo.split('.')[0] for demo in demos]
    blacklist = ('', 'index', 'portfolio-details')
    demos = [demo for demo in demos if not demo in blacklist]
    context = dict(title=f"{len(demos)} Demonstration",
                   demos=demos)
    return render(request, 'demo/index.html', context)

@xframe_options_exempt
def pixel_art(request):
    context = dict(title="Pixel-Art")
    return render(request, 'demo/pixel-art.html', context)

@xframe_options_exempt
def garage(request):
    return render(request, 'demo/garage.html', {})

@xframe_options_exempt
def calendar(request):
    return render(request, 'demo/calendar.html', {})

@xframe_options_exempt
def google_calendar(request):
    return render(request, 'demo/google-calendar.html', {})

@xframe_options_exempt
def html(request):
    return render(request, 'demo/html.html', {})

@xframe_options_exempt
def qrcode(request):
    return render(request, 'demo/qrcode.html', {})

@xframe_options_exempt
def discord(request):
    return render(request, 'demo/discord.html', {})

@xframe_options_exempt
def todolist(request):
    return render(request, 'demo/todolist.html', {})

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
