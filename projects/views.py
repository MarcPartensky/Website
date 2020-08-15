from django.shortcuts import render

# Create your views here.
def projects(request):
    render(request, 'projects/projects.html')