from django import forms
from .models import comment_text

calss CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment_text']
