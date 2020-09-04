from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    context = dict(title='Website of Marc Partensky')
    return render(request, 'home/home.html', context)

def about(request):
    context = dict(title="About Marc Partensky")
    return render(request, 'home/about.html', context)

def donation(request):
    context = dict(title='Donate to Marc Partensky')
    return render(request, 'home/donation.html', context)

def cv(request):
    context = dict(title="CV of Marc Partensky")
    return render(request, 'home/cv.html', context=context)

def contact(request):
    context = dict(title="Contact of Marc Partensky")
    return render(request, 'home/contact.html', context=context)

def date(request):
    return HttpResponse(str(datetime.datetime.now()))
