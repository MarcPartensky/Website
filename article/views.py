from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'articles': []
    }
    return render(request, 'article/index.html', context)

def read(request, title):
    return HttpResponse('This article does not exist, at least yet ...')
