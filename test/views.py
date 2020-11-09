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
    return render(request, 'test/homepage1.html', {})

def vanta_net(request):
    return render(request, 'test/vanta_net.html', {})

def programming_languages_logo(request):
    return render(request, 'test/programming_languages_logo.html', {})

def ace_editor(request):
    return render(request, 'test/ace-editor.html', {})

def codemirror_editor(request):
    return render(request, 'test/codemirror-editor.html', {})

def xterm(request):
    return render(request, 'test/xterm.html', {})

def terminal(request):
    return render(request, 'test/terminal.html', {})

def skulpt(request):
    return render(request, 'test/skulpt.html', {})

def codemirror_plus_skulpt(request):
    return render(request, 'test/codemirror+skulpt.html', {})

def todolist(request):
    return render(request, 'test/todolist.html', {})
