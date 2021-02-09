from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, null=False)
    num_doc = models.CharField(max_length=50, null=False)
    cnpj = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=True)
    address = models.IntegerField(null=False)
