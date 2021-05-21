from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    JsonResponse,
)
from .models import Url, Request, get_uuid
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def url(request: HttpRequest, route: str = None):
    """One url."""

    if request.method == "GET":
        url = Url.objects.filter(route=route).first()
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        Request(url=url, ip=ip, user=request.user).save()
        url.save()
        return HttpResponsePermanentRedirect(redirect_to=url.target)

    elif request.method == "POST":
        route = route or get_uuid()
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
            print("found so updated")
            url_found.delete()
        url.save()
        print(get_uuid())
        print(url.route)
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
            id=url.id,
            route=url.route,
            target=url.target,
            description=url.description,
            created=str(url.created),
            updated=str(url.updated),
            author=(url.author.id if url.author else None),
        )
        for url in Url.objects.all()
    ]
    return JsonResponse(dict(urls=urls), safe=True)


def requests(request: HttpRequest):
    """Return the list of all requests."""
    requests = [
        dict(
            id=request.id,
            url=request.url.id,
            ip=request.ip,
            timestamp=request.timestamp,
            user=(request.user.id if request.user else None),
        )
        for request in Request.objects.all()
    ]
    return JsonResponse(dict(requests=requests), safe=True)
