from django.db import models
from django.utils import timezone

class Provider(models.Model):
    company_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=50, null=True)
    cnpj = models.CharField(max_length=20, null=False)
    status = models.BooleanField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.company_name)
