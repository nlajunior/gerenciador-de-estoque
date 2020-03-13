import locale

class AbstractModel():
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    def format_money(self, value):
        valor = value
        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            valor = locale.currency(valor, grouping=True, symbol=None)
        except:
            pass

        return 'R$%s' % valor
