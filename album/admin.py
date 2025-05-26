from django.contrib import admin
from .models import Album, Photo, PhotoComment

# Register your models here.


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'user', 'status']
    list_filter = ['user']
    ordering = ['user', 'name']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'album']
    list_filter = ['album']


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    list_display = ['photo', 'comment', 'approved']
    ordering = ['approved']
