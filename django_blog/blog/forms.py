from django import forms
from .models import User, Post


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        Model = User
        fields = ['username', 'email']


class PostForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ['title', 'content']