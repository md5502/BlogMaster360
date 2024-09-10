from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "meta_title", "body", "categories", "tags", "summary", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
