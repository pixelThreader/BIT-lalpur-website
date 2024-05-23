from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="blog"),
    path("blogs/", views.blog, name="blog"),
    path("post/", views.blog_post, name="blog_post"),
    path("search/", views.search, name="search"),
]