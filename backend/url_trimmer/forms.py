from django import forms
from . import models


class AddUrl(forms.ModelForm):

    class Meta:
        model = models.SaveURL
        fields = ('url',)
