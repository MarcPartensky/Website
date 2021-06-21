"""
Api views that don't necessarily provide a gui interface.
"""

import os
import sys
import json
import html
import random
import urllib
import subprocess

from io import StringIO
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import PermissionDenied

from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UploadFileForm, UploadMarkdownForm, TodoForm
from django.views.decorators.csrf import csrf_exempt
from .models import MarkdownModel

from todo.models import Todo


def index(request):
    return render(request, "index/index.html", {})


def test(request):
    return HttpResponse("test")


def addition(request):
    """Add a and b numbers together."""
    a = int(request.GET.get("a"))
    b = int(request.GET.get("b"))
    return HttpResponse(str(a + b))


def random_req(request):
    """Return a random number."""
    return HttpResponse(random.randint(0, 1000))


class ExampleView(APIView):
    """A view that can accept POST requests with JSON content."""

    parser_classes = [JSONParser]

    def post(self, request, format=None):
        print("receiving stuff")
        print(request.data)
        return Response({"received data": request.data})


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
    if request.method == "POST":
        print("pass")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES["file"])
            # handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect("/success/url/")
    else:
        print("did not pass")
        form = UploadFileForm()
    return HttpResponse("response")
    # return render(request, 'upload.html', {'form': form})


@csrf_exempt
def upload_markdown(request):
    """Markdown Uploader"""
    print("received markdown")
    if request.method == "POST":
        form = UploadMarkdownForm(request.POST, request.FILES)
        file = str(form.files["file"])
        filepath = f"{os.getcwd()}/media/article/{file}"
        print("trying to post:", filepath)
        content = form.files["file"].file.read().decode("utf-8")
        lines = content.split("\n")
        if lines[0].startswith("#!"):
            lines = lines[1:]
        content = "\n".join(lines).strip()
        with open(filepath, "w") as f:
            f.write(content)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponse("success")
        else:
            return HttpResponse("invalid form")
    elif request.method == "GET":
        form = UploadMarkdownForm()
        context = {
            "form": form,
        }
        return render(request, "api/upload.html", context)
    return HttpResponse("only get and post methods are allowed")


def view_markdown(request):
    context = {"markdown_object": MarkdownModel.objects.all()[0]}
    return render(request, "api/view-markdown.html", context)


users = {}


@csrf_exempt
def login(request):
    """Log api user view."""
    print(request.POST)
    user = request.POST["user"]
    password = request.POST["password"]
    print(user, password)
    print(os.environ["WEBSITE_USER"], os.environ["WEBSITE_PASSWORD"])
    if (user, password) != (os.environ["WEBSITE_USER"], os.environ["WEBSITE_PASSWORD"]):
        raise PermissionDenied
    token = int(hash(random.random()) / 1000)
    print(f"python-shell: {user} logs with {token}\n")
    users[token] = dict(locals={}, python=False, name=user)
    return HttpResponse('{"token":' + str(token) + "}")


class Capturing(list):
    """Capture print output and store it."""

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


@csrf_exempt
def python(request, cmd: str):
    """Python view."""
    cmd = html.unescape(cmd)
    token = int(request.POST["token"])
    user = users[token]
    locals_ = user["locals"]
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
        text = "\n".join([f"{line}" for line in out])
        return HttpResponse(urllib.parse.quote(text))
    except:
        text = "\n".join([f"{line}" for line in out])
        return HttpResponse(urllib.parse.quote(text), status=500)


@csrf_exempt
def todo_index(request: HttpRequest):
    """View todos or post new todo."""
    if request.method == "GET":
        todos = Todo.objects.all()
        print(todos)
        # serializer = SnippetSerializer(snippets, many=True)
        # return JsonResponse(serializer.data, safe=False)
        content = json.dumps(list(todos))
        return HttpResponse(content)

    elif request.method == "POST":
        print(request)
        form = TodoForm(request)
        if form.is_valid():
            form.save()
            return HttpResponse("ok", status=200)
        return HttpResponse("not", status=500)
        # data = JSONParser().parse(request)
        # print(data)
        # serializer = SnippetSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        # return JsonResponse(serializer.data, status=200)
        # return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def todo(request: HttpRequest, id: int):
    """View, update or delete existing todo."""
    todo = Todo.objects.filter(id=id)
    if request.method == "GET":
        content = json.dumps(todo.__dict__)
        return HttpResponse(content, mimetype="application/x-json")

    elif request.method == "POST":
        pass
    data = JSONParser().parse(request)

    # return Json


def port(request: HttpRequest):
    """Return a random available port within a given range."""
    port_min = os.environ.get('PORT_MIN') or 8000
    port_max = os.environ.get('PORT_MAX') or 8099
    cmd = f"comm -23 <(seq {port_min} {port_max} | sort) <(ss -Htan | awk '{print $4}' | cut -d':' -f2 | sort -u) | shuf | head -n $port"
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout
