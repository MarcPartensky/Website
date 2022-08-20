"""
Business app used for self promoting my web services.
"""

import yaml

from rich import print
from django.http.response import JsonResponse, HttpResponse, FileResponse
from django.shortcuts import render
from home.context import hydrate, base

@hydrate(base)
def index(request, context, lang: str="fr"):
    """Business page view."""
    path = "business/text.yaml"
    with open(path, "r") as stream:
        text = yaml.safe_load(stream)
    lang = request.GET.get('lang') or lang
    context.update(text[lang])
    print(context)
    if request.GET.get("json"):
        return JsonResponse(text)
    if request.GET.get("yaml") or request.GET.get("yml"):
        return FileResponse(
            open(path, "rb"),
            filename="business.yml",
            content_type="application/x-yaml"
        )
    return render(request, "business/business.html", context)

@hydrate(base)
def offers(request, context):
    """Offers page view."""
    return render(request, "business/offers.html", context)
