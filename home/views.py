from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    context = dict(title='Website of Marc Partensky')
    return render(request, 'home/home.html', context)

def about(request):
    context = dict(title="About Marc Partensky")
    return render(request, 'home/about.html', context)

def donation(request):
    context = dict(title='Donate to Marc Partensky')
    return render(request, 'home/donation.html', context)

def cv(request):
    context = dict(title="CV of Marc Partensky")
    return render(request, 'home/cv.html', context=context)

def contact(request):
    context = dict(title="Contact of Marc Partensky")
    return render(request, 'home/contact.html', context=context)

def date(request):
    return HttpResponse(str(datetime.datetime.now()))

# HTTP Errors
def bad_request(request, exception):
    response = render(
        request,
        'error/400.html',
    )
    response.status_code = 400
    return response

def permission_denied(request, exception):
    response = render(
        request,
        'error/404.html',
    )
    response.status_code = 404
    return response

def page_not_found(request, exception):
    response = render(
        request,
        'error/403.html',
    )
    response.status_code = 403
    return response

def server_error(request):
    response = render(
        request,
        'error/500.html',
    )
    response.status_code = 500
    return response
