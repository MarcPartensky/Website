from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import GamePost, GamePostComment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

# Create your views here.
def games(request):
    context = dict(
        title="games",
        gameposts=GamePost.objects.all(),
        gamepostcomments=GamePostComment.objects.all(),
    )
    return render(request, 'games/games.html', context=context)

class GamePostListView(ListView):
    model = GamePost
    template_name = 'games/games.html'
    context_object_name = 'gameposts'
    ordering = ['-timestamp']

class GamePostDetailView(DetailView):
    model = GamePost

class GamePostCreateView(LoginRequiredMixin, CreateView):
    model = GamePost
    fields = ['title', 'content', 'thumbnail', 'play']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# class GamePostUpdateView(UpdateView)

