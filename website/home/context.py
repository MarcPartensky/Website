"""Return the context of the views in the home section."""

# import datetime
import re
import os

import requests
import datetime

from article.context import get_articles
from django_project.settings import DEBUG


def get_github_info():
    """Use github api to fetch informations about my account."""
    context = {}

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
        text = requests.get("https://github.com/marcpartensky/").text

        pattern = r'<span title=\"(\d+)\" class="Counter ">\d+</span>'
        context["github_repos_number"] = re.findall(pattern, text)[0]

        pattern = r"(\d+)</span>\n +followers"
        context["github_followers"] = re.findall(pattern, text)[0]

        pattern = r"(,|\d)+ contributions"
        # print(re.findall(pattern, text))
        context["github_year_commits"] = re.findall(pattern, text)[0]

        pattern = r"Created (,|\d+)+\n +commits? in\n +(,|\d+)+\n +repositor(ies|y)"
        # print(text, re.findall(pattern, text))
        result = re.findall(pattern, text)
        context["github_month_commits"] = result[0][0]
        context["github_month_commits_repos"] = result[0][1]
    except Exception:
        # print('except')
        context["github_repos_number"] = 0
        context["github_followers"] = 0
        context["github_year_commits"] = 0
        context["github_month_commits"] = 0
        context["github_month_commits_repos"] = 0

        text = requests.get("https://github.com/marcpartensky/").text

        # print(text)

        pattern = r'<span title=\"(\d+)\" class="Counter ">\d+</span>'
        # print(re.findall(pattern, text))

        pattern = r"(\d+)</span>\n +followers"
        # print(re.findall(pattern, text))

        pattern = r"(,|\d)+ contributions"
        # print(re.findall(pattern, text))

        pattern = r"Created (,|\d+)+\n +commits? in\n +(,|\d+)+\n +repositor(ies|y)"
        # print(re.findall(pattern, text))

    url = "https://api.github.com/repos/marcpartensky/website/commits"
    response = requests.get(url).json()
    if len(response):
        context["date"] = response[0]["commit"]["author"]["date"]

    return context


def get_theme(request):
    """Return the right css file for the theme."""
    context = {}
    if "theme" in request.GET:
        context["theme"] = request.GET["theme"]
    else:
        context["theme"] = "light"
    return context


def get_demos():
    """Return the context with demos."""
    demos = os.listdir(f"{os.getcwd()}/demo/templates/demo")
    demos = [demo.split(".")[0] for demo in demos]
    blacklist = ("", "index", "portfolio-details")
    demos = [demo for demo in demos if not demo in blacklist]
    return dict(demos=demos)


def get_vanta():
    """Return the context of the vanta config."""
    # print('debug for vanta:', DEBUG)
    if DEBUG:
        vanta_points = 0.1
    else:
        vanta_points = 10.0
    return dict(vanta_points=vanta_points)


# def get_articles():
#     """Return the articles."""
#     return {}


def get_games():
    """Return the games."""
    return {}


def get_calendar_url():
    """Return the calendar url."""
    # calendar_url = "https://open-web-calendar.herokuapp.com/calendar.html?specification_url=https://gist.githubusercontent.com/MarcPartensky/1c20873acf6a628bd38b4ace58527838/raw/facf84c8caf648ca19c554043c685fec77865134/calendar.json"

    calendar_url = "https://calendar.marcpartensky.com/calendar.html?specification_url=https://gist.githubusercontent.com/MarcPartensky/1c20873acf6a628bd38b4ace58527838/raw/facf84c8caf648ca19c554043c685fec77865134/calendar.json"
    return dict(calendar_url=calendar_url)


def get_marc_age():
    """Return the age of Marc computed."""
    birth = datetime.datetime(year=2000, month=1, day=12)
    now = datetime.datetime.now()
    delta = now - birth
    return dict(marc_age=delta.days // 365)


def home(request):
    """Return the home context."""
    # context = dict(title='Website of Marc Partensky')
    return dict(
        **get_github_info(),
        **get_theme(request),
        **get_demos(),
        **get_articles(),
        **get_vanta(),
        **get_games(),
        **get_calendar_url(),
        **get_marc_age(),
    )


def base(request):
    """Return the base context."""
    # context = dict(title='Website of Marc Partensky')
    return dict(
        **get_theme(request),
        **get_demos(),
        **get_articles(),
        **get_vanta(),
        **get_games(),
    )


def fake_base(request):
    """Return a fake base context to avoid connecting to third parties."""
    return dict(
        theme="dark",
        **get_vanta(),
    )


# def combine_dicts(dicts):
#     d = {}
#     for di in dicts:
#         d.update(di)
#     return d


def hydrate(*context_getters, debug=False):
    """Double decorator that updates the context."""

    def view_decorator(view):
        """Decorator view."""

        def view_decorated(request, *args, context: dict = {}, **kwargs):
            """Decorated view."""
            context_hydrated = {}
            for context_getter in context_getters:
                context_hydrated.update(context_getter(request))
            context.update(context_hydrated)
            # if debug: print(context)
            return view(request, *args, context=context, **kwargs)

        return view_decorated

    return view_decorator
