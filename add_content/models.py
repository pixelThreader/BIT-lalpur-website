from django.db import models

# Create your models here.

class Faculty(models.Model):

    sno = models.AutoField(primary_key=True)
    facultyID = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=2000)
    department = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    joined_on = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=1000)
    localhost = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=255)
    phone_office = models.CharField(max_length=255)
    faculty_email = models.CharField(max_length=500)
    teaching_year = models.CharField(max_length=255)
    research_year = models.CharField(max_length=255)
    research_area = models.TextField()
    publications = models.TextField()
    image = models.ImageField(upload_to="uploads/faculty_profile/", blank=True)

    class Meta:
        verbose_name = ("faculty")
        verbose_name_plural = ("faculty")

    def __str__(self):
        return self.name

class notification(models.Model):

    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    uptime = models.DateTimeField(auto_now_add=True)
    notificationID = models.CharField(max_length=255)

    

    class Meta:
        verbose_name = ("notification")
        verbose_name_plural = ("notifications")

    def __str__(self):
        return self.name
