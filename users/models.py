from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=128, blank = True)
    last_name = models.CharField(max_length=128, blank = True)
    position = models.CharField(max_length=128, blank = True)
    contact_number = models.CharField(max_length=128, blank = True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])
