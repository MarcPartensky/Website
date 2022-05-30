from django.shortcuts import render
import requests
import html


def random_quote(lang="en"):
    url = "https://quotes15.p.rapidapi.com/quotes/random/"
    querystring = {"language_code": lang}
    headers = {
        "x-rapidapi-host": "quotes15.p.rapidapi.com",
        "x-rapidapi-key": "9f89a4d69emsh51b4e1005159b42p14a115jsn521840e553e7",
    }
    d = requests.request("GET", url, headers=headers, params=querystring).json()
    return dict(
        id=d["id"],
        content=html.unescape(d["content"]),
        author=d["originator"]["name"],
        url=d["originator"]["url"],
        full_url=d["url"],
        tags=d["tags"],
    )


# Create your views here.
def touch_typing(request):
    context = dict(title="touch typing")
    context.update(dict(quote=random_quote()))
    return render(request, "touch-typing/touch-typing.html", context=context)
