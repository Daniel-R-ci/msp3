from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages

from django.http import Http404
from django.http import HttpResponseRedirect

from .models import Album, Photo, PhotoComment
from .forms import (
    CreateAlbumForm,
    EditAlbumForm,
    AddPhotoForm,
    EditPhotoForm,
    CommentForm
)


# Create your views here.

# Check if user is a member of ShutterClickers
def check_if_member(user):
    """
    Returns true if logged in member is member of ShutterClickers
    """
    # Code for checking membership in groups found at Stackoverflow.com
    return user.groups.filter(name='Members').exists()


# Supply view to albums.html
def album_list(request):
    """
    Supplies data to albums.html:
    return {
    albums_preview, user_is_member, create_album_form, own_albums, has_albums
    }
    """

    # Check for posting of new album
    if request.method == "POST":
        create_album_form = CreateAlbumForm(data=request.POST)
        if create_album_form.is_valid():
            album = create_album_form.save(commit=False)
            album.user = request.user
            album.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Album created. You need to change the status to Publish to make it visible for all visitors.' # noqa
            )

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

    # Get the users own albums, and a boolean to tell template if ablums exist
    own_albums = []
    has_albums = False
    if check_if_member(request.user):
        own_albums = Album.objects.filter(user=request.user)
        if own_albums.count() > 0:
            has_albums = True

    # Reset the create album form
    create_album_form = CreateAlbumForm()

    return render(
        request,
        "album/albums.html",
        {
            "albums_preview": albums_preview,
            "user_is_member": check_if_member(request.user),
            "create_album_form": create_album_form,
            "own_albums": own_albums,
            "has_albums": has_albums
        }
    )


# Supply view to album.html
def album_view(request, album_id):
    """
    Supplies data to album.html:
    return {
    album, photo_count, photo_pack, user_is_member, user_is_owner,
    edit_album_form, add_photo_form"
    }
    """

    # Get the requested album and associated photos
    try:
        album = Album.objects.get(pk=album_id)
    except Exception:
        raise Http404

    # Raise Http404 for albums with status DRAFT is not users own
    if request.user != album.user and album.status == Album.Status.DRAFT:
        raise Http404

    # For template to know if user is owner of album
    if request.user == album.user:
        user_is_owner = True
    else:
        user_is_owner = False

    photos = album.photos.all()
    photo_count = photos.count()

    # Count number of approved comments for each photo
    comment_count = []
    for photo in photos:
        comment_count.append(photo.comments.filter(approved=True).count())

    # Zip photos and comment_count
    photo_pack = zip(photos, comment_count)

    edit_album_form = EditAlbumForm()
    add_photo_form = AddPhotoForm()

    return render(
        request,
        "album/album.html",
        {
            "album": album,
            "photo_count": photo_count,
            "photo_pack": photo_pack,
            "user_is_member": check_if_member(request.user),
            "user_is_owner": user_is_owner,
            "edit_album_form": edit_album_form,
            "add_photo_form": add_photo_form
         }
    )


# Supplies view to photo.html
def photo_view(request, photo_id):
    """
    Supplies data to photo.html:
    return{
    photo, photocomments, photocomments_count, comment_form,
    edit_photo_form, user_is_member
    }
    """

    # Get the requested photo
    queryset = Photo.objects.all()
    photo = get_object_or_404(queryset, pk=photo_id)

    # Raise 404 if album status has been set to DRAFT
    # and current user is not album owner
    if photo.album.status == Album.Status.DRAFT and photo.album.user != request.user: # noqa
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
    edit_photo_form = EditPhotoForm()

    # Read all photocomments and calculate number of approved comments
    photocomments = photo.comments.all().order_by("-created_on")
    photocomments_count = photo.comments.filter(approved=True).count()

    return render(
        request,
        "album/photo.html",
        {"photo": photo,
         "photocomments": photocomments,
         "photocomments_count": photocomments_count,
         "comment_form": comment_form,
         "edit_photo_form": edit_photo_form,
         "user_is_member": check_if_member(request.user)
         }
    )


# Edit album
def album_edit(request, album_id):
    """
    Edit album:
    Raises 404 or returns to album
    """

    if request.method == "POST":
        queryset = Album.objects.all()
        album = get_object_or_404(queryset, pk=album_id)

        # Raise Http404 if current user is not album user
        if album.user != request.user:
            raise Http404

        album_form = EditAlbumForm(data=request.POST, instance=album)
        if album_form.is_valid():
            album = album_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Album successfully updated!"
            )

    return HttpResponseRedirect(reverse('album', args=[album_id]))


# Delete album
def album_delete(request, album_id):
    """
    Delete album:
    Raises 404 or returns to albums
    """

    queryset = Album.objects.all()
    album = get_object_or_404(queryset, pk=album_id)

    if album.user == request.user:
        album.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Your album has ben deleted'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own albums!'
        )
    return HttpResponseRedirect('/albums/')


# Add a photo to album
def photo_add(request, album_id):
    """
    Add photo to album
    Raises 404 or returns to album
    """

    # Raises Http404 if current user is not album user
    queryset = Album.objects.filter(user=request.user)
    album = get_object_or_404(queryset, pk=album_id)

    if request.method == "POST":
        add_photo_form = AddPhotoForm(request.POST, request.FILES)
        if add_photo_form.is_valid():
            photo = add_photo_form.save(commit=False)
            photo.album = album
            photo.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your photo has been uploaded!'
            )
        else:
            print(add_photo_form.fields)
            messages.add_message(
                request, messages.ERROR,
                'Form was not valid!')
    else:
        messages.add_message(
            request, messages.ERROR,
            'Method was not post!')

    return HttpResponseRedirect(reverse('album', args=[album_id]))


# Edit information about photo
def photo_edit(request, photo_id):
    """
    Edit photo:
    Raises 404 or returns to photo
    """

    if request.method == "POST":
        queryset = Photo.objects.all()
        photo = get_object_or_404(queryset, pk=photo_id)

        # Raise Http404 if current user is not album user
        if photo.album.user != request.user:
            raise Http404

        photo_form = EditPhotoForm(data=request.POST, instance=photo)

        if photo_form.is_valid():
            photo = photo_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Photo information successfully updated!"
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                "Photo information was not updated!"
            )

    return HttpResponseRedirect(reverse('photo', args=[photo_id]))


# Delete photo
def photo_delete(request, photo_id):
    """ Delete photo:
    Raises 404 or returns to album
    """

    queryset = Photo.objects.all()
    photo = get_object_or_404(queryset, pk=photo_id)

    album_id = photo.album.pk

    if photo.album.user == request.user:
        photo.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Your photo has ben deleted!'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own photos!'
        )

    return HttpResponseRedirect(reverse('album', args=[album_id]))


# Edit comment
def photocomment_edit(request, photo_id, comment_id):
    """ Edit comment:
    Raises 404 or returns to photo
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


# Delete comment
def photocomment_delete(request, photo_id, comment_id):
    """
    Delete comment:
    Raises 404 or returns to photo
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
