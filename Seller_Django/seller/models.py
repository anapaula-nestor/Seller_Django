from django.db import models
from person.models import Person


class Seller(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
