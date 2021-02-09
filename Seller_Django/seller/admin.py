from django.contrib import admin
from seller.models import Seller


class SellerAdmin(admin.ModelAdmin):
    list_display = ('active', 'person')


admin.site.register(Seller, SellerAdmin)