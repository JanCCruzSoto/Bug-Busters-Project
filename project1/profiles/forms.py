from django import forms

from .models import profiles


class ProfileForm(forms.ModelForm):
    class Meta:
        model = profiles
        fields = [
            'email',
            'name',
            'lastName',
            'birth',
            'languages',
            'description'
        ]
