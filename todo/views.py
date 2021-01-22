from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from home.context import hydrate, base
from . import forms
from . import models

@login_required
def todo(request, context:dict={}):
    """View main todos."""
    # todos = models.Todo.objects.filter()
    return render(request, 'todo/todo.html', context)


# @user_passes_test(lambda u:u.is_superuser)
@staff_member_required
def todo_state(request, context:dict={}):
    """List todo states."""
    context['todo_states'] = models.TodoState.objects.all()
    return render(request, 'todo/todo_state.html', context)

def todo_done(request, context:dict={}):
    """View main todos done."""
    return render(request, 'todo/todo_done.html', context)


def todo_new(request, context:dict={}):
    """View new todos."""
    if request.method == 'POST':
        redirect(reverse('todo'))
        form = forms.TodoForm(request.POST)
        form.save()
        redirect('/')

    form = forms.TodoForm()
    context['form'] = form
    return render(request, 'todo/todo_new.html', context)

def todo_add(request, context:dict={}):
    """View add todos."""
    # return render(request, 'todo/todo_add.html', context)

def todo_update(request, id, context:dict={}):
    """View update todos."""
    # return render(request, 'todo/todo_update.html', context)

def todo_delete(request, id, context:dict={}):
    """View delete todos."""
    # return render(request, 'todo/todo_delete.html', context)

