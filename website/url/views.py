from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    JsonResponse,
)
from django.core.exceptions import PermissionDenied
from .models import Url, Request, get_uuid
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def url(request: HttpRequest, route: str = None):
    """One url."""
    print('redirected from url/views.py:url')

    if request.method == "GET":
        url = Url.objects.filter(route=route).first()
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        if isinstance(request.user, User):
            user = request.user
        else:
            user = None
        Request(url=url, ip=ip, user=user).save()
        url.save()
        return HttpResponsePermanentRedirect(redirect_to=url.target)

    elif request.method == "POST":
        route = route or get_uuid()
        url = Url.objects.filter(route=route).first()
        if not url:
            if isinstance(request.user, User):
                author = request.user
            else:
                author = None
            url = Url(
                route=route,
                target=request.POST.get("target"),
                description=request.POST.get("description"),
                author=author,
            )
        elif request.user == url.author:
            url.target = request.POST.get("target")
            url.description = request.POST.get("description")
        else:
            raise PermissionDenied
        url.save()
        print(request.META)
        scheme = request.META.get("HTTP_X_FORWARDED_PROTO") or request._get_scheme()
        print(get_uuid())
        print(url.route)
        return HttpResponse(scheme + "://" + request.get_host() + "//" + url.route)

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
