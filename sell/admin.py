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
    list_display = ("__str__", 'is_payed', 'date',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    exclude = ('slug',)
