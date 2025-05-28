from django import forms
from .models import Album, Photo, PhotoComment
from cloudinary.forms import CloudinaryFileField


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


class AddPhotoForm(forms.ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = Photo
        fields = (
            'title',
            'description',
            'technical',
            'image',
        )


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = (
            'title',
            'description',
            'technical',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('comment',)
