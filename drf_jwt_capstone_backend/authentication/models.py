from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=12)
    profile_pic = models.ImageField(null=True, blank=True)
    rating = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):

        return (f"{self.first_name} {self.last_name}")
