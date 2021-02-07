from django.shortcuts import render
from home.context import hydrate, base


@hydrate(base)
def index(request, context):
    return render(request, "business/business.html", context)


@hydrate(base)
def offers(request, context):
    return render(request, "business/offers.html", context)
