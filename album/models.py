from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

###########################################
# ALBUM MODELS
# ALL MODELS RELATING TO ALBUM APP
###########################################


class Album(models.Model):
    """
    Album: Contains photo album, belong to -user-
    """

    class Status(models.TextChoices):
        """
        Text choices, to show if album is publish or in draft status
        """
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    name = models.CharField(max_length=200)
    description = models.CharField(
        max_length=200,
        blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="albums"
    )
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    public_album = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns album.name by user
        """
        return f"{self.name} - by {self.user}"


class Photo(models.Model):
    """
    Photo: Photograph belonging in -album-
    """

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="photos"
    )
    title = models.CharField(
        max_length=25,
        blank=True
    )
    description = models.CharField(
        max_length=250,
        blank=True
    )
    technical = models.CharField(
        max_length=250,
        blank=True
    )
    image = CloudinaryField('image')

    def __str__(self):
        """
        Returns image: PK (title) album.name by user
         """
        if self.title != "":
            msg = (
                f"image{self.pk}: {self.title} in {self.album.name}"
                f" by {self.album.user}"
            )
            return msg

        return f"image{self.pk} in {self.album.name} by {self.album.user}"


class PhotoComment(models.Model):
    """
    PhotoComment, belonging to -photo-, written by -user-
    """

    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter"
    )
    comment = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        """
        Return Comment on photo PK by user
        """
        return f"Comment on photo {self.photo.pk} by {self.user}"
