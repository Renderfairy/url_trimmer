from django import forms
from . import models


class AddUrl(forms.ModelForm):
    """Saves url instance to databease.
    """
    class Meta:
        model = models.URL
        fields = ('url',)
