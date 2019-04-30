from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import status

from wish.models import Wish, Comment
from wish.serializers import CommentSerializer


class WishesView(View):
    template_name = 'wishes.html'

    def get(self, request, *args, **kwargs):
        wishes = Wish.objects.all().order_by("name")
        return render(request, self.template_name, {'wishes': wishes})


class CommentsView(View):
    template_name = 'comments.html'

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.filter(wish=kwargs.get('wish_id')).order_by("-created")
        return render(request, self.template_name, {'comments': comments})

    def post(self, request, *args, **kwargs):
        try:
            wish = Wish.objects.get(pk=kwargs.get('wish_id'))
            data = dict(
                name=request.POST.get("name"),
                comment=request.POST.get("comment"),
                wish=wish.pk
            )
            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                comment = serializer.save()
                messages.add_message(request, messages.INFO, 'Kommentar tilføjet.')
                return JsonResponse({'created': True})
            else:
                return JsonResponse({'created': False}, status=status.HTTP_400_BAD_REQUEST)
        except Wish.DoesNotExist:
            JsonResponse({'created': False}, status=status.HTTP_404_NOT_FOUND)