from django.shortcuts import render
from .models import GamePost, GamePostComment
# Create your views here.
def games(request):
    context = dict(
        title="games",
        gameposts=GamePost.objects.all(),
        gamepostcomments=GamePostComment.objects.all(),
    )
    return render(request, 'games/games.html', context=context)