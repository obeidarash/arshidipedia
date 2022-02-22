from django.contrib import admin
from .models import InvoiceItem, Invoice, Product
from .forms import InvoiceAdminForm


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 0


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    form = InvoiceAdminForm
    inlines = (InvoiceItemInline,)
    list_display = ("__str__", 'is_payed', 'date', 'link_to_invoice',)

    def link_to_invoice(self, obj):
        # todo: create url in html
        return f"<a href=\"invoice/{obj.id}\" target=\"_blank\"></a>"

    link_to_invoice.short_description = 'link'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    exclude = ('slug',)
