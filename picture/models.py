from django.db import models


class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/')
