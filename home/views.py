from django.shortcuts import render

def home(request):
    context = dict(title='Website of Marc Partensky')
    return render(request, 'home/home.html', context)