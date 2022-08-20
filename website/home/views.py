import os
import subprocess

from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from home.context import hydrate, home, base
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from rich import print

from . import models
from . import forms


@hydrate(home)
def home(request, context={}):
    # context = get_home_context(request)
    print(context)
    return render(request, "home/home.html", context)


@hydrate(base)
def about(request, context={}):
    context["title"] = "About Marc Partensky"
    return render(request, "home/about.html", context)


@hydrate(base)
def donation(request, context={}):
    context["title"] = "Donate to Marc Partensky"
    return render(request, "home/donation.html", context)


@hydrate(base)
def cv(request, context={}):
    context["title"] = "CV of Marc Partensky"
    return render(request, "home/cv.html", context)


@hydrate(base)
def cv_1p(request, context={}):
    # context = get_base_context(request)
    context["title"] = "CV of Marc Partensky"
    return render(request, "home/cv-1p.html", context)


@hydrate(base)
def contact(request, context={}):
    context["title"] = "Contact Marc Partensky"
    return render(request, "home/contact.html", context)


@hydrate(base)
def resume(request, context={}):
    return render(request, "home/resume.html", {})


@csrf_protect
def notified_mail_form(request):
    """View that receives email adresses send in forms footers."""
    try:
        d = dict(email=request.POST["email"])
        if request.user.is_authenticated:
            d.update(dict(user=request.user))
        print(d)
        form = forms.NotifiedMailListForm(d)
        if form.is_valid():
            print("success")
            messages.success(request, "Form submission successful.")
            form.save()
            return HttpResponse("success", status=200)
        else:
            messages.error(request, "Form submission error.", extra_tags="danger")
            print("invalid form")
            # print('Added to mail list successfully.')
            return HttpResponse(str(form.errors.as_text()), status=500)
        # return HttpResponse("not connected", status=403)
    except Exception as e:
        return HttpResponse("Something went wrong: " + str(e), status=500)


@hydrate(base)
def notified_mail_list(request, context: dict = {}):
    """View that shows notified people."""
    context["notified_list"] = models.NotifiedMailList.objects.all()
    return render(request, "home/notified_mail_list.html", context)


db_graph_extensions = [
    "png",
    "svg",
    "jpeg",
    "jpg",
    "tiff",
]


def db_graph(request, extension: str):
    """Return database graph in png format."""
    path = f"media/assets/img/db_graph.{extension}"
    print("image path:", path)
    if extension not in db_graph_extensions:
        raise PermissionDenied
    cache = False
    print(request.GET)
    if request.GET.get("cache"):
        print(request.GET["cache"])
        cache = request.GET["cache"].lower() == "true"
    if not cache:
        command = f"python manage.py graph_models -a -o {path}"
        print(f"[yellow]running[/]: [magenta]{command}[/]")
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            process.wait()
            print("[yellow]process over[/]:", process.returncode)
        except Exception as e:
            print(f"[red]failed[/]: {e}")
    else:
        print("loading from cache")
    with open(path, "rb") as img:
        # response = FileResponse(img.read())
        t = img.read()
    # print('loaded response')
    response = HttpResponse(t, content_type=f"image/{extension}")
    return response


# HTTP Errors
# def bad_request(request, exception):
# response = render(
# request,
# 'error/400.html',
# )
# response.status_code = 400
# return response

# def permission_denied(request, exception):
# response = render(
# request,
# 'error/404.html',
# )
# response.status_code = 404
# return response

# def page_not_found(request, exception):
# response = render(
# request,
# 'error/403.html',
# )
# response.status_code = 403
# return response

# def server_error(request):
# response = render(
# request,
# 'error/500.html',
# )
# response.status_code = 500
# return response
