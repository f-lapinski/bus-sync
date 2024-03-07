from django.db import models


class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    inv_number = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.brand} {self.model} [{self.register_number}] [{self.inv_number}]"