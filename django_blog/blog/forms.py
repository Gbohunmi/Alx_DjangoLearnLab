from django import forms
from .models import User, Post, Comment
from taggit.forms import TagWidget, TagField
#widgets


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        Model = User
        fields = ['username', 'email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    tags = TagField(widget=TagWidget())

    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'content']
