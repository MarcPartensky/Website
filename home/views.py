from django.shortcuts import render
from django.http import HttpResponse

from . import models
import requests
import datetime
import re

def home(request):
    context = dict(title='Website of Marc Partensky')


    # url = 'https://api.github.com/users/marcpartensky'
    # d = requests.get(url).json()

    # context['github_repos_number'] = d['public_repos']
    # context['github_followers'] = d['followers']
    # context['github_year_commits'] = d['followers']

    # url = 'https://api.github.com/users/marcpartensky/events'
    # d = requests.get(url).json()

    # print(len(d))


    # repos = requests.get('https://api.github.com/users/marcpartensky/repos').text
    # context['github_repos_number']= len(repos)
    # print(len(repos))

    # r = requests.get('https://api.github.com/users/marcpartensky/followers')
    # context['github_followers'] = len(r.text)

    try:
        text = requests.get('https://github.com/marcpartensky/').text

        pattern = '<span title=\"(\d+)\" class="Counter ">\d+</span>'
        context['github_repos_number'] = re.findall(pattern, text)[0]

        pattern = '(\d+)</span>\n +followers'
        context['github_followers'] = re.findall(pattern, text)[0]

        pattern = '(,|\d)+ contributions'
        # print(re.findall(pattern, text))
        context['github_year_commits'] = re.findall(pattern, text)[0]

        pattern = 'Created (,|\d+)+\n +commits? in\n +(,|\d+)+\n +repositor(ies|y)'
        print(text, re.findall(pattern, text))
        result = re.findall(pattern, text)
        context['github_month_commits'] = result[0][0]
        context['github_month_commits_repos'] = result[0][1]
    except:
        print('except')
        context['github_repos_number'] = 0
        context['github_followers'] = 0
        context['github_year_commits'] = 0
        context['github_month_commits'] = 0
        context['github_month_commits_repos'] = 0

        text = requests.get('https://github.com/marcpartensky/').text

        # print(text)

        pattern = r'<span title=\"(\d+)\" class="Counter ">\d+</span>'
        print(re.findall(pattern, text))

        pattern = r'(\d+)</span>\n +followers'
        print(re.findall(pattern, text))

        pattern = r'(,|\d)+ contributions'
        print(re.findall(pattern, text))

        pattern = r'Created (,|\d+)+\n +commits? in\n +(,|\d+)+\n +repositor(ies|y)'
        print(re.findall(pattern, text))
    finally:
        print('wtf')

    if 'theme' in request.GET:
        context['theme'] = request.GET['theme']
    else:
        context['theme'] = 'light'
    url = 'https://api.github.com/repos/marcpartensky/website/commits'
    response = requests.get(url).json()
    context['date'] = response[0]['commit']['author']['date']
    print(context)
    return render(request, 'home/home.html', context)

def about(request):
    context = dict(title="About Marc Partensky")
    return render(request, 'home/about.html', context)

def donation(request):
    context = dict(title='Donate to Marc Partensky')
    return render(request, 'home/donation.html', context)

def cv(request):
    context = dict(title="CV of Marc Partensky")
    return render(request, 'home/cv.html', context)

def cv_1p(request):
    context = dict(title="CV of Marc Partensky")
    return render(request, 'home/cv-1p.html', context)

def contact(request):
    context = dict(title="Contact of Marc Partensky")
    return render(request, 'home/contact.html', context)

def resume(request):
    return render(request, 'home/resume.html', {})

def mail_form(request):
    """View that receives email adresses."""
    try:
        notified_mail = models.NotifiedMailList(request.POST['email'])
        notified_mail.save()
        return HttpResponse('Added to mail list successfully.')
    except:
        HttpResponse('Something went wrong', status=500)

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
