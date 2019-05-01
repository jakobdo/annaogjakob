from django.db import models


class Music(models.Model):
    artist = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
