from django.shortcuts import render
from .models import Album, Photo

# Create your views here.


def album_list(request):
    """
    Retrieves album_preview (zip) to use in album/index.html |
    Zip contains albums (all public albums),
    photos (up to three photos for each album),
    photo_counts (total number of picture in albums)
    """

    # Get all published albums
    albums = Album.objects.filter(status=Album.Status.PUBLISHED)

    photos = []
    photo_counts = []

    # Get up two three photos for each album, and total number of photos
    for a in albums:
        fkey = a.pk
        photoquery = Photo.objects.filter(album=fkey)
        photo_counts.append(photoquery.count())
        preview_photos = []
        for i in range(photoquery.count()):
            preview_photos.append(photoquery[i])
            if i == 2:
                break

        photos.append(preview_photos)

    # Technic to use zip to send objects together to DJANGO templates found at
    # https://stackoverflow.com/questions/67961063/django-template-using-forloop-counter-as-an-index-to-a-list
    albums_preview = zip(albums, photos, photo_counts)

    return render(
        request,
        "album/albums.html",
        {
            "albums_preview": albums_preview
        }
    )
