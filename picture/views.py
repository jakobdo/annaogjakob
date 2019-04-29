from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View

from picture.forms import PictureForm
from picture.models import Picture


class PicturesView(View):
    template_name = 'pictures.html'

    def get(self, request, *args, **kwargs):
        picture_listing = Picture.objects.all()
        paginator = Paginator(picture_listing, 10)
        page = request.GET.get('page')
        pictures = paginator.get_page(page)
        return render(request, self.template_name, {'pictures': pictures})

    def post(self, request, *args, **kwargs):
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Bilede gemt.')
        else:
            messages.add_message(request, messages.ERROR, 'Bilede IKKE gemt.')
        return redirect('pictures')
