from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    JsonResponse,
)
from .models import Url, get_uuid
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def url(request: HttpRequest, route: str = None):
    """One url."""

    if request.method == "GET":
        url = Url.objects.filter(route=route).first()
        url.count += 1
        url.save()
        return HttpResponsePermanentRedirect(redirect_to=url.target)

    elif request.method == "POST":
        if route == "":
            route = get_uuid()
        print("route")
        if isinstance(request.user, User):
            url = Url(
                route=route,
                target=request.POST.get("target"),
                description=request.POST.get("description"),
                author=request.user,
            )
        else:
            url = Url(
                route=route,
                target=request.POST.get("target"),
                description=request.POST.get("description"),
            )
        url_found = Url.objects.filter(route=route).first()
        if url_found:
            url_found.delete()
        url.save()
        return HttpResponse(
            request._get_scheme() + "://" + request.get_host() + "/u" + url.route
        )

    # elif request.method == "PUT":
    #     url = Url.objects.filter(route=route).first()
    #     url.route = request.PUT.get("route") or url.route
    #     url.target = request.PUT.get("target") or url.target
    #     url.description = request.PUT.get("description") or url.description
    #     url.save()
    #     return HttpResponse("url saved")


def urls(request: HttpRequest):
    """Return the list of all urls."""
    urls = [
        dict(
            route=url.route,
            target=url.target,
            description=url.description,
            author=str(url.author),
        )
        for url in Url.objects.all()
    ]
    return JsonResponse(dict(urls=urls), safe=True)
