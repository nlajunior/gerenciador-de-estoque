from django.db import models
from . import Category, Provider

class Product(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.TextField(null=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    provider = models.ManyToManyField(Provider, null=True)
    value = models.FloatField(default=0.0)
    status = models.BooleanField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)