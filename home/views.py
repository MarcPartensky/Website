from django.shortcuts import render

def home(request):
    context = dict(title='Website of Marc Partensky')
    return render(request, 'home/home.html', context)

def about(request):
    context = dict(title="About Marc Partensky")
    return render(request, 'home/about.html', context)

def donation(request):
    context = dict(title='Donate to Marc Partensky')
    return render(request, 'home/donation.html', context)