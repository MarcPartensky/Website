from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def hello(request):
    return HttpResponse("Hello World")

def date(request):
    r = HttpResponse(str(datetime.datetime.now()))
    return HttpResponse(str(datetime.datetime.now()))

a = 1
def count(request):
    global a
    a += 1
    return HttpResponse(str(a))

def url(request):
    return HttpResponse(request.path)

def args(request):
    return HttpResponse(request.content_params)

def user_agent(request):
    return HttpResponse(request.headers.get('user-agent'))

def addition(request):
    print(request.GET)
    # args = request.path.split('?')[1]
    # args = args.split('&')
    # n = sum(map(int, args))
    a, b, c = map(request.GET.__getitem__, 'abc')
    return HttpResponse(str(n))

def decompose_prime(request):
    request
    return HttpResponse()

def homepage1(request):
    return render(request, 'tests/homepage1.html', {})

def vanta_net(request):
    return render(request, 'tests/vanta_net.html', {})

def programming_languages_logo(request):
    return render(request, 'tests/programming_languages_logo.html', {})
