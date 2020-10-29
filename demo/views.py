from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def demo(request):
    context = dict(title="Demonstration")
    return render(request, 'demo/demo.html', context)

def pixel_art(request):
    context = dict(title="Pixel-Art")
    return render(request, 'demo/pixel_art.html', context)

def garage(request):
    return render(request, 'demo/garage.html', {})

def google_calendar(request):
    return render(request, 'demo/google_calendar.html', {})

def google_official_calendar(request):
    return render(request, 'demo/google_official_calendar.html', {})

def html(request):
    return render(request, 'demo/html.html', {})

def qrcode(request):
    return render(request, 'demo/qrcode.html', {})

def discord(request):
    return render(request, 'demo/discord.html', {})
