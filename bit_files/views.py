from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bit_files/index.html')

def files(request):
    return render(request, 'bit_files/files.html')

def preview(request):
    return render(request, 'bit_files/preview.html')

def download(request):
    return render(request, 'bit_files/download.html')