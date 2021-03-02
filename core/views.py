from django.shortcuts import render
from .models import Album
from .models import Artist

# Create your views here.

def index(request):
    albums = Album.objects.all()
    return render(request, 'html/index.html', {'albums':albums})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'html/artists.html', {'artists': artists})