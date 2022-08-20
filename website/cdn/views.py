from django.shortcuts import render

# Create your views here.


def cdn(request):
    return render(request, "cdn/cdn.js", {})


def test(request):
    return render(request, "cdn/test.html", {})
