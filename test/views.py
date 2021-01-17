"""
Test views made for testing before deploying.
"""

import datetime

from django.shortcuts import render
from django.http import HttpResponse

from home.context import hydrate, base


def hello(request):
    """Send hello world."""
    return HttpResponse("Hello World")

def date(request):
    """Send the currente datetime."""
    return HttpResponse(str(datetime.datetime.now()))

state = dict(a=0)
def count(request):
    """Count how many times this request was called.."""
    state['a'] += 1
    return HttpResponse(str(state['a']))

def url(request):
    """Send back the very same url that was requested."""
    return HttpResponse(request.path)

def args(request):
    """Send the parsed http argumnts of the get request."""
    return HttpResponse(request.content_params)

def user_agent(request):
    """Return the http user agent."""
    return HttpResponse(request.headers.get('user-agent'))

def addition1(request, *numbers):
    """Add 2 integers together."""
    print(numbers)
    n = sum(*numbers)
    return HttpResponse(str(n))

def addition2(request):
    """Add parameters without messing with url path."""
    print('get parameters:', request.GET)
    # args = request.path.split('?')[1]
    # args = args.split('&')
    # n = sum(map(int, args))
    a, b, c = map(request.GET.__getitem__, 'abc')
    return HttpResponse(str(n))

def decompose_prime(request):
    """Decompose a number into its decompositionof prime
    factors."""
    # Not done
    request
    return HttpResponse()

def homepage1(request):
    """Return the homepage 1."""
    return render(request, 'test/homepage1.html', {})

def vanta_net(request):
    """Return a test of vanta."""
    return render(request, 'test/vanta_net.html', {})

def programming_languages_logo(request):
    """Return a list of programming languages logo."""
    return render(request, 'test/programming_languages_logo.html', {})

def ace_editor(request):
    """Return an ace editor."""
    return render(request, 'test/ace-editor.html', {})

def codemirror_editor(request):
    """Return a code mirror editor."""
    return render(request, 'test/codemirror-editor.html', {})

def xterm(request):
    """Return an xterm terminal."""
    return render(request, 'test/xterm.html', {})

def skulpt(request):
    """Return the use case of skulpt."""
    return render(request, 'test/skulpt.html', {})

def codemirror_plus_skulpt(request):
    """Return a combination of skulpt and codemirror."""
    return render(request, 'test/codemirror+skulpt.html', {})

def todolist(request):
    """Return a deprecated version of a todolist."""
    return render(request, 'test/todolist.html', {})

def discordbot(request):
    """Return an iframe produced by discord."""
    return render(request, 'test/discordbot.html', {})

# def mdeditor(request):
    # """Return a md editor."""
#     return render(request, 'tes')

@hydrate(base)
def websocket(request, context):
    """Test websocket and channels."""
    return render(request, 'test/websocket.html', context)

@hydrate(base)
def valentin(request, context):
    """C'est la page de valentin c'est pas moi."""
    return render(request, 'test/valentin.html', context)

@hydrate(base)
def paul(request, context):
    """C'est la page de paul c'est pas moi."""
    return render(request, 'test/paul.html', context)
