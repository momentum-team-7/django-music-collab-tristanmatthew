from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ArtistForm, AlbumForm
from .models import Album, Artist


# Create your views here.

def index(request):
    albums = Album.objects.all().order_by('artist', 'pk')
    return render(request, 'html/index.html', {'albums':albums})


def artist_list(request):
    artists = Artist.objects.all().order_by('artist', 'pk')
    return render(request, 'html/artists.html', {'artists':artists})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'html/artist_detail.html', {'artist': artist})


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'html/album_list.html', {'albums':albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'html/album_detail.html', {'album':album})

def add_artist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArtistForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/artists')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArtistForm()

    return render(request, 'html/add_artist.html', {'form': form})

def edit_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artists')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'html/edit_artist.html', {'form': form, 'artist':artist })

def delete_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return HttpResponseRedirect('/artists')

def add_album(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlbumForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/album-list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlbumForm()

    return render(request, 'html/add_album.html', {'form': form})


def edit_album(request, pk):
    # get the instance of the Artist model from the database
    album = get_object_or_404(Album, pk=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlbumForm(request.POST, instance=album)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/album-list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlbumForm(instance=album)
    return render(request, 'html/edit_album.html', {'form': form, 'album':album })

def delete_album(request, pk):
    artist = get_object_or_404(Album, pk=pk)
    artist.delete()
    return HttpResponseRedirect('/album-list')


