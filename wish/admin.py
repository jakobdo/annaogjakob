from django.contrib import admin

from wish.models import Wish, Comment


class WishAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wish, WishAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)