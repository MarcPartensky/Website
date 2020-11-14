from django.shortcuts import render
from django.http import HttpResponse
import random

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

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    """A view that can accept POST requests with JSON content."""
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        print(request.data)
        return Response({'received data': request.data})
