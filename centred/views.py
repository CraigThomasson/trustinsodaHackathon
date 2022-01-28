from django.shortcuts import render

# Create your views here.
def centred_index(request):
    return render(request, "centred/index.html")