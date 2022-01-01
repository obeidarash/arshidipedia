from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name_fa', 'lastname_fa', 'gender', )
    search_fields = ('name_fa', 'lastname_fa', )
