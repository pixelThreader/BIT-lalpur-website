from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def blog(request):
    return render(request, 'blog/blog.html')

def blog_post(request):
    return render(request, 'blog/blog_post.html')

def search(request):
    return render(request, 'blog/search.html')

