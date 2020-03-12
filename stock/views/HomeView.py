from ..orm import AbstractOrm
from ..models import User, Order
from django.shortcuts import render
from django.db.models import Sum
class HomeView():

    def __init__(self):
        self.abstractOrm = AbstractOrm()
        self.user = User()
        self.order = Order()

    def index(self, request):
        context = {
            'last_orders': Order.objects.order_by('-date').all()[:4],
            'higher_sales': Order.objects.order_by('-total_value').all()[:4],
            'week_orders': {
                'canceled': self.order.get_order(3),
                'pending': self.order.get_order(2),
                'finish': self.order.get_order(1)
            }
        }
        return render(request, template_name='home.html', context=context)

