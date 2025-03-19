from django import forms
from .models import User


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        Model = User
        fields = ['username', 'email']