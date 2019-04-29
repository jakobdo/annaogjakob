from django.db import models
from django.urls import reverse


class Wish(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_comments(self):
        return reverse("wish_comments", kwargs=dict(wish_id=self.id))

    class Meta:
        verbose_name_plural = "wishes"


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.comment}"
