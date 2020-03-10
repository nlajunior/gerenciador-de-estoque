from ..models import User
from ..forms.GenericForm import GenericForm
from .AbstractView import AbstractView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class UserView():
    def __init__(self):
        self.view = AbstractView()
        self.formClass = GenericForm(User, exclude=('password',))

    def index(self, request):
        return self.view.index(request=request, model=User, pagina='User', headers=['email', 'Ações'], template_html='list-user.html')

    def form(self, request, id=None):
        return self.view.form(request, User, self.formClass.getForm(), 'users', 'user', 'Novo usuário', 'Usuário', id, request.FILES)

    def delete(self, request, id):
        return self.view.delete(request, User, 'users', id)

    def login(self, request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        next = request.GET.get('next')
                        if next is not None:
                            if next == '/logout':
                                return redirect("/dashboard")
                            else:
                                return redirect(next)
                        else:
                            return redirect("/dashboard")
                else:
                    result = {
                        'message': 'Usuário não encontrado',
                        'type': messages.ERROR
                    }
                    messages.add_message(request, result['type'], result['message'])
            else:
                result = {
                    'message': 'Login ou senha Inválidos',
                    'type': messages.ERROR
                }
                messages.add_message(request, result['type'], result['message'])

            context = {
                'form': form
            }
            return render(request, 'login.html', context)
        else:
            if not request.user.is_anonymous:
                return redirect("/dashboard")

            form = AuthenticationForm()
            context = {
                'form': form,
                'pagina': 'Login'
            }

            return render(request, 'login.html', context)


    def logout(self, request):
        try:
            logout(request)
            del request.session['username']
        except:
            pass
        return redirect("/login")

