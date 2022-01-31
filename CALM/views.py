# Create your views here.

def base(request):
    return render(request, 'site_base.html')

def about(request):
    return render(request, 'about.html')
    
def solutions(request):
    return render(request, 'solutions.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')