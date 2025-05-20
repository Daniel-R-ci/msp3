from django.contrib import admin
from .models import Album, Photo

# Register your models here.


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'user', 'status']
    list_filter = ['user']
    ordering = ['user', 'name']


admin.site.register(Photo)
