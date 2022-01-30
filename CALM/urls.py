from .views import base, solutions, about
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',  base),
    path('solutions/',  solutions),
    path('about/',  about),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
