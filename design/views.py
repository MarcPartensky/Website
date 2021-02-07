from django.shortcuts import render

# Create your views here.


def design(request):
    return render(request, "design/design.html", {})


def test_1(request):
    return render(request, "design/test_1.html", {})
