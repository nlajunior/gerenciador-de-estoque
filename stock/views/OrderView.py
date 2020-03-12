from ..orm import AbstractOrm
from ..models import Order
from ..forms.GenericForm import GenericForm
from .AbstractView import AbstractView

class OrderView():
    def __init__(self):
        self.abstractOrm = AbstractOrm()
        self.view = AbstractView()
        self.formClass = GenericForm(Order, fields='__all__')

    def index(self, request):
        return self.view.index(request=request, model=Order, pagina='Order', headers=['Pedido', 'Valor Total', 'Quantidade', 'Status', 'Data de Criação', 'Quantidade', 'Ações'],
                               template_html='list-order.html', permissions_roles=[1, 2, 3])

    def form(self, request, id=None):
        return self.view.form(request, Order, self.formClass.getForm(), 'orders', 'order', 'Novo pedido', 'Pedidos', id, permissions_roles=[1, 2, 3])

    def delete(self, request, id):
        return self.view.delete(request, Order, 'orders', id, permissions_roles=[1, 2, 3])