from django.db import models
from django.db import transaction
from django.contrib import messages
from . import User, Product
import locale
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
        if self.product.quantity >= self.quantity:
            try:
                with transaction.atomic():
                    self.product.quantity -= self.quantity
                    self.product.save()
                    super().save(*args, **kwargs)
                messages.add_message(kwargs['request'], messages.SUCCESS, 'Pedido salvo com sucesso.')
            except:
                messages.add_message(kwargs['request'], messages.ERROR, 'Ocorreu um erro ao salvar o pedido.')
        else:
            messages.add_message(kwargs['request'], messages.ERROR, 'A quantidade excede o total de produtos.')

    def format_money(self):
        valor = self.total_value
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor = locale.currency(valor, grouping=True, symbol=None)
        return 'R$%s' % valor

    def get_order(self, status):
        total = [0, 0, 0, 0, 0, 0, 0]
        start_date = datetime.today() - timedelta(days=7)
        end_date = datetime.today()
        for i, r in enumerate(Order.objects.values('date').filter(status=status).filter(date__range=(start_date, end_date)).annotate(dcount=Count('date'))):
            total[i] = r['dcount']

        return total