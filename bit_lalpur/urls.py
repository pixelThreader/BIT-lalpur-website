"""
URL configuration for bit_lalpur project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import urls as HURLS
from add_content import urls as ADDURL
from administration_bit import urls as ADMINURL
from blog import urls as BURLS
from contact import urls as CURLS
from mailHandler import urls as MHURLS

admin.site.site_header = "BIT LALPUR"
admin.site.site_title = "BIT LALPUR"
admin.site.index_title = "BIT LALPUR"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(HURLS)),
    path("upload/", include(ADDURL)),
    path("administration/", include(ADMINURL)),
    path("blog/", include(BURLS)),
    path("contact/", include(CURLS)),
    path("mails/", include(MHURLS)),
]
