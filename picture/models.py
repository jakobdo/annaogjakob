from django.db import models


class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
