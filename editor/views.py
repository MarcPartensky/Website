from django.shortcuts import render

# Create your views here.

def index(request):
    """Show all code projects."""
    return render(request, 'editor/index.html', {})

projects = {}
def project(request, id:str):
    """Show a code project."""
