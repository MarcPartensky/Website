from django import forms
from .models import MarkdownModel

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class UploadMarkdownForm(forms.ModelForm):
    class Meta:
        model = MarkdownModel
        fields = ('title', 'file', )


    # def save(self, *args, **kwargs):
    #     print('saving model somewhere')
    #     print(args, kwargs)
    #     return super().save(*args, **kwargs)
