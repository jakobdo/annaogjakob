from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from picture.views import CameraView, PicturesView
from wish.views import WishesView, CommentsView
from comment.views import CommentsView as GuestCommentsView
from music.views import MusicView

urlpatterns = [
    path('', TemplateView.as_view(template_name='welcome.html'), name="welcome"),
    path('info/', TemplateView.as_view(template_name='info.html'), name="info"),
    path('wishes/', WishesView.as_view(), name="wishes"),
    path('wishes/<wish_id>/comments/', CommentsView.as_view(), name="wish_comments"),
    path('guests/', GuestCommentsView.as_view(), name="guests"),
    path('pictures/', PicturesView.as_view(), name="pictures"),
    path('camera/', CameraView.as_view(), name="camera"),
    path('music/', MusicView.as_view(), name="music"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
