from django import forms

class GenericForm(forms.ModelForm):
    def __init__(self, model, fields=None, exclude=None, *args, **kwargs):
        super(GenericForm).__init__(*args, **kwargs)
        self.model = model
        self.fields = fields
        self.exclude = exclude

    def getForm(self):
        class Form(forms.ModelForm):
            class Meta:
                model = self.model
                try:
                    if self.fields is not None:
                        fields = self.fields
                    else:
                        exclude = self.exclude
                except:
                    fields = '__all__'

        return Form