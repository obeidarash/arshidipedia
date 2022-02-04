from django.contrib import admin
from .models import PayAttach


@admin.register(PayAttach)
class PayAttachAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)
