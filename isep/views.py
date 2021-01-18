from django.shortcuts import render

from home.context import base, hydrate

# Create your views here.

@hydrate(base)
def isep(request, context:dict={}):
    """Affiche une page sur l'isep."""
    context = dict(isep='isep')
    return render(request, 'isep/isep.html', context)

@hydrate(base)
def app(request, context:dict={}):
    """Affiche les groupes d'App."""
    context['app'] = 'app'
    return render(request, 'isep/app.html', context)

@hydrate(base)
def planning_app(request, context:dict={}):
    """Affiche le planning d'App info."""
    return render(request, 'isep/planning_app.html', context)

@hydrate(base)
def lignee(request, context:dict={}):
    """Affiche les lignées à l'Isep."""
    return render(request, 'isep/lignee.html', context)

def garage(request, context:dict={}):
    """Blaqgue pour le garage"""
    return render(request, 'isep/garage.html', context)
