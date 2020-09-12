from django.shortcuts import render

# Create your views here.

def isep(request):
    context = dict(isep='isep')
    return render(request, 'isep/isep.html', context)

def app(request):
    context = dict(app='app')
    return render(request, 'isep/app.html', context)
