from django.forms import ModelForm

from picture.models import Picture


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['picture']
