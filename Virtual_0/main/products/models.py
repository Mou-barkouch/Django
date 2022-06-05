from unicodedata import category
from django.db import models

# Create your models here.

class Product(models.Model):
    x =  [
        ("banana", "banana"),
        ("apple", "Apple")
    
    ]

    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True,choices=x)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Phone'
        ordering = ['-price'] # -:desc

    class Test(models.Model):
        date = models.DateField()
