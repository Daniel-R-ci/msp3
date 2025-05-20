from . import views
from django.urls import path

urlpatterns = [
    # path('', views.album_list, name='albums'),
    path('', views.Album_List.as_view(), name='albums'),
]