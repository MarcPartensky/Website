from django.shortcuts import render, HttpResponse
from .models import ArticleModel

# Create your views here.
def index(request):
    context = {
        'articles': []
    }
    return render(request, 'article/index.html', context)

def read(request, title):
    return HttpResponse('This article does not exist, at least yet ...')

