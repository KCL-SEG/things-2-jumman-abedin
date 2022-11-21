"""Forms of the project."""
from django import forms
from .models import Thing


class ThingForum(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widget = {'description': forms.Textarea(), 'quantity': forms.NumberInput()}
