from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from .models import GamePost, GamePostComment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.
def game(request):
    context = dict(
        title="game",
        gameposts=GamePost.objects.all(),
        gamepostcomments=GamePostComment.objects.all(),
    )
    return render(request, 'game/game.html', context=context)

class GamePostListView(ListView):
    model = GamePost
    template_name = 'game/game.html'
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

class GamePostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GamePost
    fields = ['title', 'content', 'thumbnail', 'play']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class GamePostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = GamePost
    success_url = "/game"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

