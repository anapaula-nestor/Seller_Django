from django.contrib import admin
from person.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_doc', 'cnpj', 'phone', 'address')


admin.site.register(Person, PersonAdmin)