from .views import index, solutions, about
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',  index),
    path('solutions/',  solutions),
    path('about_us/',  solutions),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)