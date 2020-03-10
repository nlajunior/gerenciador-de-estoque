from ..orm import AbstractOrm
from ..models import Provider
from ..forms.GenericForm import GenericForm
from .AbstractView import AbstractView

class ProviderView():
    def __init__(self):
        self.abstractOrm = AbstractOrm()
        self.provider = Provider()
        self.view = AbstractView()
        self.formClass = GenericForm(Provider, fields='__all__')

    def index(self, request):
        return self.view.index(request=request, model=Provider, pagina='Fornecedor', headers=['Empresa', 'E-mail', 'CNPJ', 'Status', 'Data de Criação', 'Ações'],
                               template_html='list-provider.html')

    def form(self, request, id=None):
        return self.view.form(request, Provider, self.formClass.getForm(), 'providers', 'provider', 'Novo fornecedor', 'Fornecedores', id)

    def delete(self, request, id):
        return self.view.delete(request, Provider, 'providers', id)