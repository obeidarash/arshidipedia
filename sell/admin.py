from django.contrib import admin
from .models import Sell


@admin.register(Sell)
class SellAdmin(admin.ModelAdmin):
    list_display = ('to_user',)
    search_fields = ('to_user',)
    autocomplete_fields = ('to_user', 'to_company')
