"""
Models required for the todolist system.
"""

from django.db import models
from django.contrib.auth.models import User

class StateTodo(models.Model):
    """Represent the state of a todo.
    Examples states are:
        - todo
        - in progress
        - done
    These are inspired from TFS."""
    title = models.CharField(mex_length=255, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(add_now=True)

    def __str__(self):
        """Return the title of the state."""
        return self.title

class StateTodolist(models.Model):
    """Represent the state of a todolist.
    Example states are:
        - todo
        - in progress
        - done
    These are inspired from TFS."""
    title = models.CharField(mex_length=255, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(add_now=True)

    def __str__(self):
        """Return the title of the state."""
        return self.title


class Todo(models.Model):
    """Represent something todo.
    A todo can be shared between multiple persons and multiple todolists."""
    content = models.TextField()
    title = models.CharField(null=True, max_length=255, unique=True)
    duration = models.DurationField(null=True)
    parent = models.OneToOneField(Todo, on_delete=models.CASCADE)
    state = models.OneToOneField(StateTodo, on_delete=models.PROTECT)
    # done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(add_now=True)

    def __str__(self):
        """Return a string representation of a todo."""
        return f"{self.pk}:{self.content}({self.title or ''}) [{self.created}|{self.updated}] {self.state}"

    @property
    def url(self):
        """Return the easiest to read url."""
        return f"https://todo/{self.title or self.pk}"

class Todolist(models.Model):
    """List of todos.
    Make use of many to many relationship of django to refer to the todolists
    since one todo can exist in multiple todolists and a todolist contains
    todos."""
    title = models.CharField(null=True, max_length=255, unique=True)
    description = models.TextField()
    todos = models.ManyToManyField(Todo)
    state = models.OneToOneField(StateTodolist, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(add_now=True)

    @property
    def url(self):
        """Return the easiest to read url."""
        return f"https://todolist/{self.title or self.pk}"

class TodoAssignment(models.Model):
    """Assignment of a user to a todo."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    todo = models.OneToOneField(Todo, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(add_now=True)

class TodolistAssignment(models.Model):
    """Assignment of a user to a todolist."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    todolist = models.OneToOneField(Todolist, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(add_now=True)

class Event(models.Model):
    """Represent an event of an activity."""
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(add_now=True)

class Calendar(models.Model):
    """Calendar of a user."""
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(add_now=True)

class Activity(models.Model):
    """Represent an activity."""
    events = models.ManyToManyField(Event)
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(add_now=True)


# class Task(models.Model):
#     """Model to represent a """
