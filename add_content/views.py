from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'add_content/index.html')

def content_faculty_upload(request):
    return render(request, 'add_content/faculty_upload.html')

def notification(request):
    return render(request, 'add_content/notification.html')

def notice(request):
    return render(request, 'add_content/notice.html')

def gallery(request):
    return render(request, 'add_content/gallery.html')

