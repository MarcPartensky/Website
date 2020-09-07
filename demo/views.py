from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = dict(title="Demonstration", projects=projects, tb=range(3))
    return render(request, 'demo/home.html', context)

def pixel_art(request):
    context = dict(title="Pixel-Art")
    return render(request, 'demo/pixel_art.html', context)
