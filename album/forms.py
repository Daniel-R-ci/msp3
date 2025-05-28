from django import forms
from .models import Album, PhotoComment


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = (
            'name',
            'description',
        )


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = (
            'name',
            'description',
            'status',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('comment',)
