from django.db import models
from django.utils.timezone import now

# Create your models here.



class Downloadable(models.Model):

    sno = models.AutoField(primary_key=True, db_index=True, unique=True)
    filename = models.CharField(max_length=500, default=None)
    downloadable_link = models.TextField(default=None)
    file = models.FileField(upload_to='downloadables/', max_length=100, default=None)
    file_made_available = models.DateTimeField(auto_now=False, auto_now_add=False, default=now)

    class Meta:
        verbose_name = ("downloadable")
        verbose_name_plural = ("downloadables")

    def __str__(self):
        return self.filename
