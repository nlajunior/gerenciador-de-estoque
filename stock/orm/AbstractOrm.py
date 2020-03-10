from django.shortcuts import render

class AbstractOrm:
    def save_or_update(self, obj):
        try:
            return obj.save()
        except Exception as e:
            raise Exception("Erro ao criar: %s" % e)

    def list(self, obj, first=False):
        try:
            if first:
                return obj.objects.first()
            return obj.objects.all()
        except Exception as e:
            print(e)
            return []

    def delete(self, obj):
        try:
            return obj.save()
        except Exception as e:
            raise Exception("Erro ao deletar: %s" % e)

    def export(self):
        pass
