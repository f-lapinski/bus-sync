from django.db import models


class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    inv_number = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
