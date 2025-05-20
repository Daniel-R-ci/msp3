from django.shortcuts import render
from django.views import generic
from .models import Album, Photo

# Create your views here.


"""def album_list(request):
    albums_queryset = Album.objects.all()

    return render(
        request,
        "album/albums.html", 
        {'albums': albums_queryset}
    )"""


class Album_List(generic.ListView):
    queryset = Album.objects.all()
    # template_name = "post_list.html"
    template_name = "album/albums.html"
    #paginate_by = 6
