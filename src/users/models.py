from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.TextField(max_length=255)
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    date_of_employment = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} Profile'
