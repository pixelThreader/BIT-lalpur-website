from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'adminstration/index.html')

def palcements(request):
    return render(request, 'adminstration/palcements.html')
