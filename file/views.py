"""Provide restricted access to files.

This app aims to give file access in a restricted way.
"""


import os
import datetime

from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt

from django.http.response import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http.request import HttpRequest
from django.contrib import messages

from . import models


def index(request: HttpRequest):
    """Show files stored.
    Does not provide access necessarily.
    """
    return render(request, "")


def file(request: HttpRequest, id: str):
    """Return a file with a given id."""
    if request.method == "POST":
        print(request.FILES)
        models.File()

        # file = models.File()
    else:
        # if

        return FileResponse()


@login_required
def permission(request: HttpRequest, id):
    """Return permission informations."""
    return


@csrf_exempt
def access_index(request: HttpRequest):
    """Post a file and request access link for it.
    Use token for authentication."""
    if request.method == "GET":
        if request.user.is_anonymous:
            print(request.META["HTTP_USER_AGENT"])
            user_agent = request.META["HTTP_USER_AGENT"]
            if user_agent.startswith("python-requests") or user_agent.startswith(
                "curl"
            ):
                print("host:", request.get_host())

                return HttpResponse(
                    "https://" + request.get_host() + reverse("login") + " "
                )
            messages.add_message(request, messages.WARNING, "Login is required.")
            return redirect("login", permanent=False)
        token = models.Token(user=request.user)
        token.save()
        return HttpResponse(token.id)

    if request.method == "POST":
        print("test")
        if not request.POST["token"]:
            messages.add_message(request, messages.WARNING, "Token is required.")
            return redirect("f")
        # file = request.FILES["file"]
        token_id = request.POST["token"]
        token = models.Token.objects.filter(id=token_id).first()
        author = token.user

        permission_choice = request.POST.get("permission")
        expiration = request.POST.get("expiration")
        file_expiration = request.POST.get("file_expiration")
        max_count = request.POST.get("max-count")
        description = request.POST.get("description")
        public = request.POST.get("public")

        # for filestream in request.FILES.getlist("file"):

        filestream = request.FILES.popitem()[1][0]
        name = filestream.name
        print(name, filestream)
        print(type(filestream))

        file = models.File.objects.filter(name=name).first()
        print(file)

        if file:
            file.file = filestream
        else:
            file = models.File(name=name, author=author)
            file.file = filestream
            print(file.file)
            file.save()

            if file_expiration:
                file.expiration = file_expiration
            if description:
                file.description = description
            if public:
                file.public = public

            print(file.file)
            file.save()

        access = models.Access(file=file)

        if permission_choice:
            access.permission = permission_choice
        if max_count:
            access.max_count = max_count
        if expiration:
            access.expiration = expiration

        access.save()
        print(access)

        return HttpResponse(request.get_host() + "/f/" + access.id)

        return HttpResponse("No file received", status=500)


def access(request: HttpRequest, uuid: str):
    """Give a permission using a public url."""
    if request.method == "GET":

        token_id = request.GET.get("token")
        token = models.Token.objects.filter(id=token_id).first()

        access = models.Access.objects.filter(id=uuid).first()

        print(access.timestamp)
        print(access.expiration)
        print(access.timestamp + access.expiration)

        print(access.file.public)

        if access.file.public:
            print(access.file.file)
            # return HttpResponse("test")
            return FileResponse(access.file.file)

        if not token:
            return HttpResponse("Token authentication required.", status=403)

        permissions = models.Permission.objects.filter(
            file=access.file, user=request.user
        ).all()

        if not permissions and token.user != access.file.author:
            access.count += 1

            if access.count > access.max_count:
                access.active = False
                return HttpResponse("Access request count exceeded.", status=403)

            if access.timestamp + access.expiration > datetime.datetime.now():
                access.active = False
                return HttpResponse("Access expired.", status=403)

            if not access.active:
                return HttpResponse("Access closed.", status=403)

            permission = models.Permission(
                file=access.file, user=request.user, permission=access.permission
            )
            permission.save()

        access.file.update_read()

        return FileResponse(access.file)
