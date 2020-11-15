from django.shortcuts import render
from django.http import HttpResponse
import random

from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UploadFileForm, UploadMarkdownForm

from django.views.decorators.csrf import csrf_exempt

from .models import MarkdownModel

# Create your views here.

def index(request):
    return render(request, 'index/index.html', {})

def test(request):
    return HttpResponse('test')

def addition(request):
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))
    return HttpResponse(str(a+b))

def random_req(request):
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
