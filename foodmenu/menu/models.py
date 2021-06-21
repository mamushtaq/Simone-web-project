from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=64)
    quantity = models.IntegerField(default=1)
    price = models.CharField(max_length=64)
    added_to_cart = models.BooleanField(default=False)

