from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
import random

from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UploadFileForm, UploadMarkdownForm

from django.views.decorators.csrf import csrf_exempt

from .models import MarkdownModel

from io import StringIO

import html
import urllib
import sys
import os

# Create your views here.

def index(request):
    return render(request, 'index/index.html', {})

def test(request):
    return HttpResponse('test')

def addition(request):
    """Add a and b numbers together."""
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))
    return HttpResponse(str(a+b))

def random_req(request):
    """Return a random number."""
    return HttpResponse(random.randint(0, 1000))

class ExampleView(APIView):
    """A view that can accept POST requests with JSON content."""
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        print('receiving stuff')
        print(request.data)
        return Response({'received data': request.data})

class FileUploadView(APIView):
    """A view that can receive files."""
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        print(request.data)
        # file_obj = request.data['file']

        # print('received your file')
        # print(file_obj)
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)

    # @csrf_exempt
    # def as_view(self, *args, **kwargs):
    #     super().as_view(self, *args, **kwargs)


@csrf_exempt
def upload_file(request):
    """Another view that can receive files."""
    if request.method == 'POST':
        print('pass')
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['file'])
            # handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        print('did not pass')
        form = UploadFileForm()
    return HttpResponse('response')
    # return render(request, 'upload.html', {'form': form})


@csrf_exempt
def upload_markdown(request):
    """Markdown Uploader"""
    print('received markdown')
    if request.method == 'POST':
        form = UploadMarkdownForm(request.POST,request.FILES)
        file = str(form.files['file'])
        filepath = f"{os.getcwd()}/media/article/{file}"
        print('trying to post:', filepath)
        content = form.files['file'].file.read().decode('utf-8')
        lines = content.split('\n')
        if lines[0].startswith('#!'):
            lines = lines[1:]
        content = '\n'.join(lines).strip()
        with open(filepath, 'w') as f:
            f.write(content)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('invalid form')
    elif request.method == 'GET':
        form = UploadMarkdownForm()
        context = {
            'form':form,
        }
        return render(request, 'api/upload.html', context)
    return HttpResponse('only get and post methods are allowed')

def view_markdown(request):
    context = {'markdown_object': MarkdownModel.objects.all()[0]}
    return render(request, 'api/view-markdown.html', context)

users = {}

@csrf_exempt
def login(request):
    """Log api user view."""
    print(request.POST)
    user = request.POST['user']
    password = request.POST['password']
    print(user, password)
    print(os.environ['WEBSITE_USER'],os.environ['WEBSITE_PASSWORD'])
    if (user,password)!=(os.environ['WEBSITE_USER'],os.environ['WEBSITE_PASSWORD']):
        raise PermissionDenied
    token = int(hash(random.random())/1000)
    print(f"python-shell: {user} logs with {token}\n")
    users[token] = dict(locals={}, python=False, name=user)
    return HttpResponse('{"token":'+str(token)+'}')

class Capturing(list):
    """Capture print output and store it."""

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


@csrf_exempt
def python(request, cmd:str):
    """Python view."""
    cmd = html.unescape(cmd)
    token = int(request.POST['token'])
    user = users[token]
    locals_ = user['locals']
    print(f"python: {user['name']} runs \"{cmd}\" given {locals_}")
    try:
        with Capturing() as out:
            exec(cmd, globals(), locals_)
        if not out:
            try:
                with Capturing() as out:
                    exec(f"print({cmd})", globals(), locals_)
            except:
                out = []
        print(f"which returns {out}\n")
        text = '\n'.join([f"{line}" for line in out])
        return HttpResponse(urllib.parse.quote(text))
    except:
        text = '\n'.join([f"{line}" for line in out])
        return HttpResponse(urllib.parse.quote(text), status=500)
