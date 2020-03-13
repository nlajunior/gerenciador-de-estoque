from django.db import models
from . import Category, Provider, AbstractModel

class Product(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    provider = models.ManyToManyField(Provider, null=True, blank=True)
    value = models.FloatField(default=0.0)
    status = models.BooleanField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)

    def format_money(self):
        abs_model = AbstractModel()
        return abs_model.format_money(self.value)