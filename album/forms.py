from django import forms
from .models import PhotoComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('comment',)
