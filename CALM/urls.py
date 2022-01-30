from .views import index, solutions
from django.urls import path

urlpatterns = [

    path('',  index),
    path('solutions.html',  solutions),
]