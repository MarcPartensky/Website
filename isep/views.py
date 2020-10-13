from django.shortcuts import render

# Create your views here.

def isep(request):
    context = dict(isep='isep')
    return render(request, 'isep/isep.html', context)

def app(request):
    context = dict(app='app')
    return render(request, 'isep/app.html', context)

def planning_app(request):
    return render(request, 'isep/planning_app.html', {})

def lignee(request):
    return render(request, 'isep/lignee.html', {})

def garage(request):
    return render(request, 'isep/garage.html', {})
