from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="uploads_bit"),
    path("faculty/", views.content_faculty_upload, name="upload_faculty"),
    path("notice/", views.notice, name="upload_notice"),
    path("gallery/", views.gallery, name="upload_gallery"),
    path("notification/", views.notification, name="upload_notification"),
]