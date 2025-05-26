from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import Http404
from django.http import HttpResponseRedirect

from .models import Album, Photo, PhotoComment
from .forms import CommentForm


# Create your views here.


def album_list(request):
    """
    Retrieves album_preview (zip) to use in album/index.html
    Returns { album_preview (zip) }
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
    Returns {album | photo_count | photo_pack}
    """

    # Get the requested album and associated photos
    queryset = Album.objects.filter(status=Album.Status.PUBLISHED)
    album = get_object_or_404(queryset, pk=album_id)
    photos = album.photos.all()
    photo_count = photos.count()

    # Count number of approved comments for each photo
    comment_count = []
    for photo in photos:
        comment_count.append(photo.comments.filter(approved=True).count())

    # Zip photos and comment_count
    photo_pack = zip(photos, comment_count)

    return render(
        request,
        "album/album.html",
        {
            "album": album,
            "photo_count": photo_count,
            "photo_pack": photo_pack

         }
    )


def photo_view(request, photo_id):
    """
    Get spefic photo and associated comments
    Return {photo, photocomments, photocomments_count comment_form}
    """

    # Get the requested photo
    queryset = Photo.objects.all()
    photo = get_object_or_404(queryset, pk=photo_id)

    # Raise 404 if album status has been set to DRAFT
    if photo.album.status == Album.Status.DRAFT:
        raise Http404

    # Check for posting of new comment
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.photo = photo

        # Sets approved to True if user is a member of ShutterClickers
        # Code for checking membership in groups found at Stackoverflow.com
        if request.user.groups.filter(name='Members').exists():
            comment.approved = True
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted'
            )
        else:
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    # Set a new instance of CommentForm
    comment_form = CommentForm()

    # Read all photocomments and calculate number of approved comments
    photocomments = photo.comments.all().order_by("-created_on")
    photocomments_count = photo.comments.filter(approved=True).count()

    return render(
        request,
        "album/photo.html",
        {"photo": photo,
         "photocomments": photocomments,
         "photocomments_count": photocomments_count,
         "comment_form": comment_form
         }
    )


def photocomment_edit(request, photo_id, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Photo.objects.all()
        photo = get_object_or_404(queryset, pk=photo_id)
        
        # Raise 404 if album status has been set to DRAFT
        if photo.album.status == Album.Status.DRAFT:
            raise Http404

        comment = get_object_or_404(PhotoComment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.photo = photo

            # Sets approved to True if user is a member of ShutterClickers
            # Code for checking membership in groups found at Stackoverflow.com
        if request.user.groups.filter(name='Members').exists():
            comment.approved = True
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment edited'
            )
        else:
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment edited and awaiting approval'
            )

        return HttpResponseRedirect(reverse('photo', args=[photo_id]))


def photocomment_delete(request, photo_id, comment_id):
    """
    view to delete comment
    """
    queryset = Photo.objects.all()
    photo = get_object_or_404(queryset, pk=photo_id)
    # Raise 404 if album status has been set to DRAFT
    if photo.album.status == Album.Status.DRAFT:
        raise Http404

    comment = get_object_or_404(PhotoComment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment deleted!'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own comments!'
        )
    return HttpResponseRedirect(reverse('photo', args=[photo_id]))
