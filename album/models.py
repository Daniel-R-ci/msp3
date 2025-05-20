from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

###########################################
# ALBUM CLASSES
# ALL CLASSES RELATING TO ALBUM
###########################################


"""class publishedAlbumsManager(models.Manager):
    def get_queryset(self):
        return (
            super().
"""


class Album(models.Model):
    """
    Album: Contains photo album, belong to -user-
    """
    class Status(models.TextChoices):
        """
        Text choises, to show if album is publish or in draft status
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
    updated_on = models.DateTimeField(auto_now_add=True)

    # objects = models.Manager()  # default manager
    # published = publishedAlbumsManager()  # custom manager

    def __str__(self):
        return f"{self.name} - by {self.user}"



###########################################
# ALBUM PHOTO
# ALL CLASSES RELATING TO PHOTO
###########################################


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
        if self.title != "":
            return f"image{self.pk}: {self.title} in album {self.album.name} by {self.album.user}"
        return f"image{self.pk} in album {self.album.name} by {self.album.user}"
  
