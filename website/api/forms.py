from django import forms
from .models import MarkdownModel
from todo.models import Todo


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class UploadMarkdownForm(forms.ModelForm):
    class Meta:
        model = MarkdownModel
        fields = (
            "title",
            "file",
        )

class TodoForm(forms.ModelForm):
    """Form of a todo."""
    class Meta:
        model = Todo
        fields = (
            "content",
            "title",
            "duration",
            "parent",
            "dependencies"
        )

    # def save(self, *args, **kwargs):
    #     print('saving model somewhere')
    #     print(args, kwargs)
    #     return super().save(*args, **kwargs)
