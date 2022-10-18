from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def how_to(request):
    return render(request, 'how_to.html', {})

def filters_page(request):
    return render(request, 'filters_page.html', {})