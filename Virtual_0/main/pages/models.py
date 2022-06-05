from django.db import models

# Create your models here.
"""
class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
"""

class Prod(models.Model):
    title = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    prods = models.ForeignKey(Prod, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
