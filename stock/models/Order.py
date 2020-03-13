from django.db import models
from django.db import transaction
from . import User, Product, AbstractModel
from django.db.models import Count
from datetime import datetime, timedelta

class Order(models.Model):
    date = models.DateField(auto_now_add=True)
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
        return '{} {}'.format(self.product, self.product)

    def save(self, *args, **kwargs):
        verify_quantity = False
        alter_quantity = True
        if self.id is not None:
            current_instance = Order.objects.filter(id=self.id).first()
            verify_quantity = self.quantity == current_instance.quantity
            alter_quantity = not self.status == current_instance.status
        else:
            if self.status == 3:
                alter_quantity = False

        if not verify_quantity:
            verify_quantity = self.product.quantity >= self.quantity

        if verify_quantity:
            try:
                with transaction.atomic():
                    self.total_value = self.product.value * self.quantity
                    if alter_quantity:
                        if self.product.status == 1:
                            self.product.quantity -= self.quantity

                        if self.product.status == 3:
                            self.product.quantity += self.quantity

                    self.product.save()
                    super().save(*args, **kwargs)
            except:
                raise Exception('Ocorreu um erro ao salvar o pedido')
        else:
            raise Exception('A quantidade excede o total de produtos.')

    def format_money(self):
        abs_model = AbstractModel()
        return abs_model.format_money(self.total_value)

    def get_order(self, status):
        total = [0, 0, 0, 0, 0, 0, 0]
        start_date = datetime.today() - timedelta(days=7)
        end_date = datetime.today()
        for i, r in enumerate(Order.objects.values('date').filter(status=status).filter(date__range=(start_date, end_date)).annotate(dcount=Count('date'))):
            total[i] = r['dcount']

        return total