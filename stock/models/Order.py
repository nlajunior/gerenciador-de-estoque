from django.db import models
from django.utils import timezone
from . import User, Product

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total_value = models.FloatField(default=0.0)
    status = models.IntegerField(choices=(
        (1, "Finalizado"),
        (2, "Pendente"),
        (3, "Cancelado")
    ))
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '{} {}'.format(self.date, self.product)