from . import views
from django.urls import path

urlpatterns = [
    path('', views.album_list, name='albums'),
    path('<int:album_id>', views.album_view, name='album'),
    path('<int:album_id>/edit_album/', views.album_edit, name="album_edit"),
    path('<int:album_id>/delete_album/', views.album_delete, name="album_delete"), # noqa
    path('<int:album_id>/add_photo/', views.photo_add, name="photo_add"),
    path('photo/<int:photo_id>', views.photo_view, name="photo"),
    path('photo/<int:photo_id>/edit_photo/', views.photo_edit, name="photo_edit"), # noqa
    path('photo/<int:photo_id>/delete_photo/', views.photo_delete, name="photo_delete"), # noqa
    path('photo/<int:photo_id>/edit_comment/<int:comment_id>',views.photocomment_edit, name="photocomment_edit"), # noqa
    path('photo/<int:photo_id>/delete_comment/<int:comment_id>', views.photocomment_delete, name="photocomment_delete") # noqa
]
