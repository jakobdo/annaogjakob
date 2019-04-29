from rest_framework import serializers

from wish.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'comment', 'wish')
