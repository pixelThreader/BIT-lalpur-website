from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdditionalUserCredentials(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)


    GENDER_CHOICE = [('Male', 'Male'), ('Female', 'Female'), ('Others','Others'), ('Not to say','Not to say')]
    WHO_CHOICE = [('Authority', 'Admin'), ('Student', 'Student'), ('Faculty', 'Faculty'), ('Staff','Staff')]

    who = models.CharField(max_length=30, choices= WHO_CHOICE)
    Emergency_id01 = models.CharField(max_length=10, unique = True)
    phone = models.CharField(max_length=20)
    phone_alt = models.CharField(max_length=20, default=None, null=True)
    gender = models.CharField(max_length=30, choices= GENDER_CHOICE)
    birth = models.DateField(auto_now=False)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pinCode = models.CharField(max_length=6)

    class Meta:
        verbose_name = "UserCredentials"
        verbose_name_plural = "AdditionalUserCredentials"

    def __str__(self):
        return self.user.username