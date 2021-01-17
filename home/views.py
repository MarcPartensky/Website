from django.shortcuts import render
from django.http import HttpResponse
from home.context import hydrate, home, base
from . import models
# from home.context import home as get_home_context
# from home.context import base as get_base_context

@hydrate(home)
def home(request, context={}):
    # context = get_home_context(request)
    print(context)
    return render(request, 'home/home.html', context)

@hydrate(base)
def about(request, context={}):
    context['title'] = "About Marc Partensky"
    return render(request, 'home/about.html', context)

@hydrate(base)
def donation(request, context={}):
    context['title'] = "Donate to Marc Partensky"
    return render(request, 'home/donation.html', context)

@hydrate(base)
def cv(request, context={}):
    context['title'] = "CV of Marc Partensky"
    return render(request, 'home/cv.html', context)

@hydrate(base)
def cv_1p(request, context={}):
    # context = get_base_context(request)
    context['title'] = "CV of Marc Partensky"
    return render(request, 'home/cv-1p.html', context)

@hydrate(base)
def contact(request, context={}):
    context['title'] = "Contact Marc Partensky"
    return render(request, 'home/contact.html', context)

@hydrate(base)
def resume(request, context={}):
    return render(request, 'home/resume.html', {})

def mail_form(request):
    """View that receives email adresses."""
    try:
        notified_mail = models.NotifiedMailList(request.POST['email'])
        notified_mail.save()
        return HttpResponse('Added to mail list successfully.')
    except:
        return HttpResponse('Something went wrong', status=500)

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
