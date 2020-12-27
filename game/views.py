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

from home.context import hydrate, base


@hydrate(base)
def game(request, context={}):
    """Render a game."""
    context.update(dict(
        title="game",
        gameposts = GamePost.objects.all(),
        gamepostcomments = GamePostComment.objects.all(),
    ))
    return render(request, 'game/game.html', context=context)

class GamePostListView(ListView):
    """List all games."""
    model = GamePost
    template_name = 'game/game.html'
    context_object_name = 'gameposts'
    ordering = ['-timestamp']

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context

class GamePostDetailView(DetailView):
    """Render a detailled view of a game."""
    model = GamePost

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context

class GamePostCreateView(LoginRequiredMixin, CreateView):
    """Create a new game."""
    model = GamePost
    fields = ['title', 'content', 'thumbnail', 'play']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context

class GamePostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update an existing game."""
    model = GamePost
    fields = ['title', 'content', 'thumbnail', 'play']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context

class GamePostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a game."""
    model = GamePost
    success_url = "/game"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context
