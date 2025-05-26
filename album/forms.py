from .models import PhotoComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('comment',)
