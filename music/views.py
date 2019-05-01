from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from music.forms import MusicForm
from music.models import Music


class MusicView(View):
    template_name = 'music.html'

    def get(self, request, *args, **kwargs):
        music = Music.objects.order_by("artist", "song")
        return render(request, self.template_name, {'music': music})

    def post(self, request, *args, **kwargs):
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Musikønske gemt.')
        else:
            messages.add_message(request, messages.ERROR, 'Musikønske IKKE gemt.')
        return redirect('music')
