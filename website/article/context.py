"""Return the context of the articles."""

import os
import random

from . import models

# from home.context import (
#     get_github_info,
#     get_theme,
#     get_demos,
#     get_articles,
#     get_games
# )

# from home.context import get_github_info
# from home.context import get_theme


# class ArticleObject:
#     """Article object."""

#     @classmethod
#     def create(cls, title:str):
#         """Create an article given its title."""
#         with open(f"{os.getcwd()}/media/article/{title}", "r") as f:
#             preview = str(f.read())[:496]+" ..."
#         title = title.replace('.md', '')
#         return cls(title, preview)

#     def __init__(self, title, preview, active=False):
#         "Create an article given its title and preview."
#         self.title = title
#         self.preview = preview
#         self.active = active

#     def __str__(self):
#         """Return the title of the article."""
#         return self.title


def get_articles_objects():
    """Return the list of article objects."""
    #     titles = os.listdir(f"{os.getcwd()}/media/article")
    #     articles = [ArticleObject.create(title) for title in titles if title!='.DS_Store']
    #     article = random.choice(articles)
    #     article.active = True
    return dict(articles=models.Article.objects.all())


def get_articles():
    """Return the list of articles."""
    #     titles = os.listdir(f"{os.getcwd()}/media/article")
    #     articles = [title.replace('.md', '') for title in titles if title!='.DS_Store']
    return dict(articles=models.Article.objects.all())


def article(request):
    """Create the context of the article view."""
    return dict(
        **get_articles_objects(),
        **get_github_info(),
        **get_theme(request),
        **get_demos(),
        **get_articles(),
        **get_games()
    )


# def article(view):
