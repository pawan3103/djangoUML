from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    baseCountry = models.CharField(max_length=256)
    currentCountry = models.CharField(max_length=256)
