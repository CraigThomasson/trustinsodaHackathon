from .views import base, solutions, about, index
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('', views.base, name="base"),
    path('index/', views.index, name="index"),
    path('solutions/',  views.solutions, name='solutions'),
    path('about/',  views.about, name='about'),
    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
