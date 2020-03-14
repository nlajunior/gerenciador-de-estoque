from django import forms

class GenericForm(forms.ModelForm):
    def __init__(self, model, fields=None, exclude=None, read_only=None, passd=None, *args, **kwargs):
        super(GenericForm).__init__(*args, **kwargs)
        self.model = model
        self.fields = fields
        self.exclude = exclude
        self.read_only = read_only
        self.passd = passd

    def getForm(self):
        class Form(forms.ModelForm):
            if self.read_only is not None:
                read_only = self.read_only
            if self.passd is not None:
                password = forms.CharField(max_length=20, min_length=3, required=True, widget=forms.PasswordInput())

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