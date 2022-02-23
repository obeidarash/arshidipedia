from django.contrib import admin
from .models import InvoiceItem, Invoice, Product
from .forms import InvoiceAdminForm
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.forms import ValidationError


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    form = InvoiceAdminForm
    inlines = (InvoiceItemInline,)
    list_display = ("__str__", 'date', 'link_to_invoice',)
    search_fields = ('id',)

    def link_to_invoice(self, obj):
        return format_html('<a href="{}" target="_blank">Go to invoice</a>', reverse('invoice', args=(obj.id,)))

    link_to_invoice.short_description = 'link'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    exclude = ('slug',)
