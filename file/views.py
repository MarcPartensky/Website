"""Provide restricted access to files.

This app aims to give file access in a restricted way.
"""


import os

from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from django.http.response import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ValidationError
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
    file = models.File.objects.filter(name=id).first()

    if not file:
        file = models.File.objects.filter(id=id).first()

        if file:
            if file.name:
                url = request.scheme + "://" + request.get_host() + "/file/" + file.name
                print(url)
                return redirect(url)

    if request.method == "GET":

        if not file:
            return HttpResponse("File does not exist.", status=404)

        if file.public:
            file.update_read()
            return FileResponse(file.file, filename=file.name)

        if not request.user.is_authenticated:
            return redirect("login", permanent=False)

        print("user:", request.user)

        permissions = models.Permission.objects.filter(
            file=file, user=request.user
        ).first()

        permissions_choices = list(
            map(lambda permission: permission.permission, permissions)
        )

        if models.PermissionChoices.READ not in permissions_choices:
            return HttpResponse("No permission to read", status=403)

        file.update_read()
        return FileResponse(file.file, filename=file.name)

    elif request.method == "POST":

        if file:

            permissions_choices = list(
                map(lambda permission: permission.permission, permissions)
            )

            if models.PermissionChoices.WRITE not in permissions_choices:
                return HttpResponse("No permission to write.", status=403)

            file.update_write()

        else:
            file = models.File(author=request.user)

        file.file = request.FILES["file"][1]

        name = request.POST.get("name")
        description = request.POST.get("description")
        public = request.POST.get("public")
        expiration = request.POST.get("expiration")

        if name:
            file.name = name

        if description:
            file.description = description

        if public is not None:
            file.public = public

        if expiration:
            file.expiration = expiration

        file.save()

    return HttpResponse("Only POST and GET requests are accepted!", status=500)


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

    elif request.method == "POST":
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

        print("public:", public)

        # for filestream in request.FILES.getlist("file"):

        filestream = request.FILES.popitem()[1][0]
        name = filestream.name

        file = models.File.objects.filter(name=name).first()

        if file:
            file.file = filestream
        else:
            file = models.File(name=name, author=author)
            file.file = filestream
            print(file.file)

        if file_expiration:
            file.expiration = file_expiration
        if description:
            file.description = description
        if public is not None:
            file.public = public

        print("file.public:", file.public)

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

    return HttpResponse("Only POST and GET requests are accepted!", status=500)


@csrf_exempt
def access(request: HttpRequest, uuid: str):
    """Give a permission using a public url."""
    if request.method == "GET":

        token_id = request.GET.get("token")
        try:
            token = models.Token.objects.filter(id=token_id).first()
        except ValidationError as e:
            return HttpResponse("Unknown token.", status=404)

        access = models.Access.objects.filter(id=uuid).first()
        if not access:
            return HttpResponse("Unknown access.", status=404)

        print("timestamp:", access.timestamp)
        print("expiration:", access.expiration)
        print("expiration timestamp:", access.timestamp + access.expiration)

        print("public:", access.file.public)
        print("access:", access)

        if access.file.public:
            print("file:", access.file.file)
            # return HttpResponse("test")
            return FileResponse(access.file.file, filename=file.name)

        print("token:", token)

        if not token:
            return HttpResponse("Token authentication required.", status=403)

        permissions = models.Permission.objects.filter(
            file=access.file, user=token.user
        )

        print("permissions:", permissions)

        print(bool(permissions))

        if not permissions and token.user != access.file.author:
            access.count += 1
            print("access.count:", access.count)

            if access.count > access.max_count:
                access.active = False
                return HttpResponse("Access request count exceeded.", status=403)

            print(access.timestamp + access.expiration)
            print(timezone.now())
            if access.timestamp + access.expiration < timezone.now():
                access.active = False
                return HttpResponse("Access expired.", status=403)

            if not access.active:
                return HttpResponse("Access closed.", status=403)

            permission = models.Permission(
                file=access.file, user=token.user, permission=access.permission
            )
            permission.save()

        print("access.file:", access.file)
        access.file.update_read()

        return FileResponse(access.file.file, filename=access.file.name)

    return HttpResponse("Only GET requests are accepted!", status=500)
