from django.db import models

class Category(models.Model):
    name = models.CharField(null=False, max_length=30)

    def __str__(self):
        return '{}'.format(self.name)