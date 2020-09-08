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
    context = dict(title="Demonstration"))
    return render(request, 'demo/demo.html', context)

def pixel_art(request):
    context = dict(title="Pixel-Art")
    return render(request, 'demo/pixel_art.html', context)
