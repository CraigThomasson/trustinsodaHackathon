from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def base(request):
    return render(request, 'site_base.html')

def solutions(request):
    return render(request, 'solutions.html')

def about(request):
    return render(request, 'about.html')