from django.contrib import admin
from .models import InvoiceItem, Invoice, Product


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1


@admin.register(Invoice)
class PostAdmin(admin.ModelAdmin):
    inlines = (InvoiceItemInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    exclude = ('slug',)
