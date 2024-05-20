from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
