from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Album(models.Model):
    title = models.CharField(max_length=280)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, blank=True, null=True, related_name="albums")
    label = models.CharField(max_length=150, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    produced_by = models.CharField(max_length=100, blank=True, null=True)
    mixed_by = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="albums")


    def __str__(self):
        return f"{self.title} | {self.artist} | {str(self.release_year)} | {self.label} | {self.produced_by} | {self.mixed_by}"

class Artist(models.Model):
    artist = models.CharField(max_length=280)
    name = models.CharField(max_length=280, blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    biography = models.CharField(max_length=2500, blank=True, null=True)


    def __str__(self):
        return f"{self.artist} | {self.name} | {self.genre} | {self.biography}"

class Image(models.Model):
    title = models.CharField(max_length=280)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title