from django import forms
from .models import Artist, Album


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist', 'genre']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['image', 'title', 'artist', 'label', 'release_year', 'produced_by', 'mixed_by']
