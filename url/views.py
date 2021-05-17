from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Url

# Create your views here.
def url(request: HttpRequest, target: str):
    """One url."""

    if request.method == "GET":
        url = Url()
        return HttpResponseRedirect(redirect_to=url)

    elif request.method == "POST":
        title = request.POST["title"]
        url = request.POST["url"]
        url = Url(url, title)
        url.save()

    return "test"


def urls():
    """Return the list of all urls."""
    return
