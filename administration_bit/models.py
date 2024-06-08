from django.db import models
from django.utils.timezone import now

# Create your models here.

class Notification(models.Model):

    sno = models.AutoField(primary_key=True)
    notif_desc_dtme = models.DateTimeField(auto_now=False, auto_now_add=False, null=False, default=None)
    notif_title = models.CharField(max_length=500, null=False, default=None)
    notif_desc = models.CharField(max_length=1000, null=False, default=None)
    notify_link = models.TextField(null=True, default=None)

    class Meta:
        verbose_name = ("notification")
        verbose_name_plural = ("notifications")

    def __str__(self):
        return self.notif_title


class FAQ(models.Model):

    sno = models.AutoField(primary_key=True, unique=True)
    question = models.TextField(default=None)
    answer = models.TextField()
    time_asked = models.DateTimeField(auto_now=False, auto_now_add=False, default=now)

    

    class Meta:
        verbose_name = ("FAQ")
        verbose_name_plural = ("FAQs")

    def __str__(self):
        return self.question


class Department(models.Model):

    sno = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, default=None)
    title = models.CharField(max_length=1000, default=None)
    desc = models.TextField()
    slug = models.SlugField(db_index=True)
    date_time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.name
