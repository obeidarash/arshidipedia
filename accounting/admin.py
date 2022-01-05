from django.contrib import admin
from .models import Pay, Category


@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('title', 'payer', 'category', 'price')
    search_fields = ('title', 'price',)
    autocomplete_fields = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
