from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

projects = [
    {
        'author': 'moi',
        'title': 'Asteroids',
        'content': 'Venez jouez on est bien.',
        'date_posted': '25 juin 2020'
    },
    {
        'author': 'toi',
        'title': 'osef',
        'content': 'Osef de tout',
        'date_posted': '26 juin 2020'
    },
    {
        'author': 'pablo',
        'title': 'stuff',
        'content': 'montage',
        'date_posted': '25 juin 2020'
    },
]

def home(request):
    context = dict(title="Demonstration", projects=projects, tb=range(3))
    return render(request, 'demo/home.html', context)

# class TestListView(ListView):
#     model = Post
#     template_name = 'demo/home.html' #<app>/<model>_<viewtype>.html
#     context_object_name = 'demos'
#     ordering = ['-date_posted']
#     paginate_by = 5
