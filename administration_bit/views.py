from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'administrations/index.html')

def palcements(request):
    return render(request, 'admiinstrations/palcements.html')
