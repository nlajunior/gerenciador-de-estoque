from ..orm import AbstractOrm
from ..models import Product
from ..forms.GenericForm import GenericForm
from .AbstractView import AbstractView

class ProductView():
    def __init__(self):
        self.abstractOrm = AbstractOrm()
        self.view = AbstractView()
        self.formClass = GenericForm(Product, fields='__all__')

    def index(self, request):
        return self.view.index(request=request, model=Product, pagina='Produto', headers=['Nome', 'Valor', 'Status', 'Data criação', 'Quantidade', 'Ações'],
                               template_html='list-product.html', permissions_roles=[1, 2])

    def form(self, request, id=None):
        return self.view.form(request, Product, self.formClass.getForm(), 'products', 'product', 'Novo produto', 'Produtos', id, permissions_roles=[1, 2])

    def delete(self, request, id):
        return self.view.delete(request, Product, 'products', id, permissions_roles=[1, 2])

