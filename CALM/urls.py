from .views import index, about
from django.urls import path, include

urlpatterns = [

    path('',  index),
    path('',  include('about')),
]