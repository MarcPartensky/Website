from django import forms
from . import models

class NotifiedMailForm(forms.ModelForm):
    """Form of a single mail field for being notified
    of the activities of Marc Partensky."""
    class Meta:
        model = models.Article
        fields = ('title', 'file', )
