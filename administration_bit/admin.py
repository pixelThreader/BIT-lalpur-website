from django.contrib import admin
from . models import Notification, FAQ

# Register your models here.

admin.site.register((Notification, FAQ))