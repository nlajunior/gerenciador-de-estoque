from ..orm import AbstractOrm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

class AbstractView():
    def __init__(self):
        self.abstractOrm = AbstractOrm()

    def index(self, request, model, pagina, headers, template_html, form=None):
        results = self.abstractOrm.list(model)
        return render(request, template_name=template_html, context={
            'pagina': pagina,
            'headers': headers,
            'results': results
        })

    def form(self, request, model, formClass, link_anterior, link, pagina, anterior, id=None, requestFile=None):
        requestPost = request.POST or None
        if id is not None:
            instance = get_object_or_404(model, pk=id)
            if requestFile:
                form = formClass(requestPost, requestFile, instance=instance)
            else:
                form = formClass(requestPost, instance=instance)
            text = ['Editado', 'Editar']
            new = False
        else:
            if requestFile:
                form = formClass(requestPost, requestFile)
            else:
                form = formClass(requestPost)
            text = ['Salvo', 'Salvar']
            new = True

        if request.method == 'POST':
            try:
                if form.is_valid():
                    instance = form.save()
                    instance.save()
                    result = {
                        'message': '%s com sucesso' % text[0],
                        'type': messages.SUCCESS
                    }
                    messages.add_message(request, result['type'], result['message'])
                    if new:
                        return redirect('/%s/%s' % (link, instance.pk))
            except Exception as e:
                result = {
                    'message': 'Ocorreu um erro ao %s. %s' % (text[1], e),
                    'type': messages.ERROR
                }
                messages.add_message(request, result['type'], result['message'])

        return render(request, template_name='form.html', context={
            'link_anterior': link_anterior,
            'page_form': link,
            'pagina': pagina,
            'anterior': anterior,
            'form': form,
            'id': id
        })

    def delete(self, request, model, link, id):
        instance = None
        if id is not None:
            instance = get_object_or_404(model, pk=id)

        try:
            instance.delete()
            result = {
                'message': 'Deletado com sucesso',
                'type': messages.SUCCESS
            }
        except Exception as e:
            result = {
                'message': 'Ocorreu um erro ao deletar. %s' % e,
                'type': messages.ERROR
            }

        messages.add_message(request, result['type'], result['message'])
        return redirect('/%s' % link)

