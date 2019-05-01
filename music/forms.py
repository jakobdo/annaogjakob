from django.forms import ModelForm

from music.models import Music


class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = ['artist', 'song']
