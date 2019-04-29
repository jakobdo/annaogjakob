from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import status

from comment.forms import CommentForm
from comment.models import Comment


class CommentsView(View):
    template_name = 'guests.html'

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all().order_by("-created")
        return render(request, self.template_name, {'comments': comments})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        comments = Comment.objects.all().order_by("-created")
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Kommentar tilføjet.')
        return redirect('guests')
