from django.shortcuts import render

def todo(request, context:dict={}):
    """View main todos."""
    return render(request, 'todo/todo.html', context)

def todo_done(request, context:dict={}):
    """View main todos done."""
    return render(request, 'todo/todo_done.html', context)

def todo_new(request, context:dict={}):
    """View new todos."""
    return render(request, 'todo/todo_new.html', context)

def todo_add(request, context:dict={}):
    """View add todos."""
    # return render(request, 'todo/todo_add.html', context)

def todo_update(request, id, context:dict={}):
    """View update todos."""
    # return render(request, 'todo/todo_update.html', context)

def todo_delete(request, id, context:dict={}):
    """View delete todos."""
    return render(request, 'todo/todo_delete.html', context)
