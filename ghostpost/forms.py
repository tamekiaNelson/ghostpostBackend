from django import forms
from ghostpost.models import GhostPoster


class RoastorBoastAddForm(forms.ModelForm):
    class Meta:
        model = GhostPoster
        fields = ['is_boast', 'post']
