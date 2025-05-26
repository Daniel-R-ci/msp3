from django.shortcuts import render, get_object_or_404
from .models import Album, Photo, PhotoComment
from .forms import CommentForm

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
    for album in albums:
        queryset = album.photos.all()
        photo_counts.append(queryset.count())
        preview_photos = []
        for i in range(queryset.count()):
            preview_photos.append(queryset[i])
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


def album_view(request, album_id):
    """
    Retrieves Album that matched album_id
    Returns {album | photos (all photos  | photo_count (no of photos in album)}
    """

    queryset = Album.objects.filter(status=Album.Status.PUBLISHED)
    album = get_object_or_404(queryset, pk=album_id)

    photos = album.photos.all()
    comment_count = []
    for photo in photos:
        comment_count.append(photo.comments.filter(approved=True).count())

    photo_count = photos.count()

    photo_pack = zip(photos, comment_count)

    return render(
        request,
        "album/album.html",
        {
            "album": album,
            "photo_pack": photo_pack,
            "photo_count": photo_count
         }
    )


def photo_view(request, photo_id):

    queryset = Photo.objects.all()
    photo = get_object_or_404(queryset, pk=photo_id)
    photocomments = photo.comments.all().order_by("-created_on")
    photocomments_count = photo.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.photo = photo
            comment.save()

        # Set Approved to True if posting user is member
    """
        if request.user.groups.filter(name='Members').exists():
            comment = PhotoComment.objects.all().filter(user=request.user).order_by("-created_on").first()
    """
    comment_form = CommentForm()

    return render(
        request,
        "album/photo.html",
        {"photo": photo,
         "photocomments": photocomments,
         "photocomments_count": photocomments_count,
         "comment_form": comment_form
         }
    )
