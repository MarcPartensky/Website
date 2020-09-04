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
