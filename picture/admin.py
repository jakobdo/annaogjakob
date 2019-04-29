from django.contrib import admin

from picture.models import Picture


class PictureAdmin(admin.ModelAdmin):
    pass
admin.site.register(Picture, PictureAdmin)
