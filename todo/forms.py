from django import forms
from . import models


class TodoForm(forms.ModelForm):
    """Todo form."""

    class Meta:
        model = models.Todo
        fields = '__all__'
