from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages

from django.http import Http404
from django.http import HttpResponseRedirect

from .models import Album, Photo, PhotoComment
from .forms import CreateAlbumForm, EditAlbumForm, CommentForm


# Create your views here.

def check_if_member(user):
    """
    Returns true if logged in member is member of ShutterClickers
    """
    # Code for checking membership in groups found at Stackoverflow.com
    return user.groups.filter(name='Members').exists()


def album_list(request):
    """
    Retrieves a list of albums and other items needed for Albums.html
    """

    # Check for posting of new comment
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


def album_view(request, album_id):
    """
    Retrieves Album that matched album_id
    and other items needed for album.html
    """

    # Get the requested album and associated photos
    try:
        album = Album.objects.get(pk=album_id)
    except Exception:
        raise Http404
    
    print(request.user)
    print(album.status)

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

    return render(
        request,
        "album/album.html",
        {
            "album": album,
            "photo_count": photo_count,
            "photo_pack": photo_pack,
            "user_is_member": check_if_member(request.user),
            "user_is_owner": user_is_owner,
            "edit_album_form": edit_album_form
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
         "comment_form": comment_form,
         "user_is_member": check_if_member(request.user)
         }
    )


def album_edit(request, album_id):
    """
    view to edit album
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


def album_delete(request, album_id):
    """
    view to delete album
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
