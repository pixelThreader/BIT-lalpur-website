from django.contrib import admin
from . models import Notification, FAQ, Department

# Register your models here.

admin.site.register((Notification, FAQ, Department))