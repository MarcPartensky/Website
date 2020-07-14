from django.shortcuts import render
from django.http import HttpResponse


def dummy(request):
    return HttpResponse('<h1>Blog Home</h1>')

def circle(request):
    context = dict(title='Circles')
    return render(request, 'first-site/circles.html', context)

def geometry(request):
    context = dict(title='Geometry')
    return render(request, 'first-site/geometry.html', context)

def physics(request):
    context = dict(title='Physics')
    return render(request, 'first-site/physics.html', context)

def intersection(request):
    context = dict(title='Intersection')
    return render(request, 'first-site/intersection.html', context)

def asteroids(request):
    context = dict(title='Asteroids')
    return render(request, 'first-site/asteroids.html', context)

def cube(request):
    context = dict(title='Cube')
    return render(request, 'first-site/cube.html', context)

def expanse(request):
    context = dict(title='Expanse')
    return render(request, 'first-site/expanse.html', context)

def connect4(request):
    context = dict(title='Expanse')
    return render(request, 'first-site/connect4.html', context)

def minecraft(request):
    context = dict(title='Minecraft')
    return render(request, 'first-site/minecraft.html', context)

def home(request):
    context = dict(title="Website of Marc Partensky")
    return render(request, 'first-site/index.html', context)
