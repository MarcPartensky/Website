from django import forms
from . import models


class Fileform(forms.ModelForm):
    class Meta:
        model = models.File
        fields = ("name", "file", "user")


class AccessForm(forms.ModelForm):
    class Meta:
        model = models.Access
        # fields = ("name", "", "permission")
        fields = "__all__"
