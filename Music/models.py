from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length= 40)
    album_title = models.CharField(max_length=30)

class Song(models.Model):
    song_name = models.CharField(max_length=20)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)

