from ..orm import AbstractOrm
from ..models import Category
from ..forms.GenericForm import GenericForm
from .AbstractView import AbstractView

class CategoryView():
    def __init__(self):
        self.abstractOrm = AbstractOrm()
        self.view = AbstractView()
        self.formClass = GenericForm(Category, fields='__all__')

    def index(self, request):
        return self.view.index(request=request, model=Category, pagina='Categoria', headers=['Nome', 'Ações'], template_html='list-category.html')

    def form(self, request, id=None):
        return self.view.form(request, Category, self.formClass.getForm(), 'categories', 'category', 'Nova categoria',
                                  'Categorias', id)
    def delete(self, request, id):
        return self.view.delete(request, Category, 'categories', id)