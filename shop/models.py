from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=2048)
    image = models.CharField(max_length=2048)

    def __str__(self):
        return self.title
