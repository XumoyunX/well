from contextlib import nullcontext

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    context = models.TextField()
    price = models.PositiveIntegerField()
    img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.name



class Kontak(models.Model):
    name = models.CharField(max_length=250)
    nomber = models.CharField(max_length=250)

    def __str__(self):
        return self.name