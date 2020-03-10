from ..models import User
from ..forms.GenericForm import GenericForm
from .AbstractView import AbstractView

class UserView():
    def __init__(self):
        self.view = AbstractView()
        self.formClass = GenericForm(User, exclude=('password',))

    def index(self, request):
        return self.view.index(request=request, model=User, pagina='User', headers=['email', 'Ações'], template_html='list-user.html')

    def form(self, request, id=None):
        return self.view.form(request, User, self.formClass.getForm(), 'users', 'user', 'Novo usuário', 'Usuário', id)

    def delete(self, request, id):
        return self.view.delete(request, User, 'users', id)
