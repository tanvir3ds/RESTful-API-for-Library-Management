from django import forms
from .models import Userprofile


class createForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = [
            'img',
            'user'
        ]