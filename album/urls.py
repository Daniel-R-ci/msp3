from . import views
from django.urls import path

urlpatterns = [
    path('', views.album_list, name='albums'),
    path('<int:album_id>', views.album_view, name='album'),
    path('photo/<int:photo_id>', views.photo_view, name="photo"),
    path(
        'photo/<int:photo_id>/edit_comment/<int:comment_id>',
        views.photocomment_edit, name="photocomment_edit"
    ),
    path(
        'photo/<int:photo_id>/delete_comment/<int:comment_id>',
        views.photocomment_delete, name="photocomment_delete"
    ),
]
