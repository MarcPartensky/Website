from django.shortcuts import render

# Create your views here.
def games(request):
    context = dict(title="games")
    return render(request, 'games/games.html', context=context)