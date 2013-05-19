from django.forms import ModelForm
from django import forms

from models import Post, Comment, Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'date']

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='')

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

