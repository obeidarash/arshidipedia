from django.contrib import admin
from .models import InvoiceItem, Invoice, Product
from .forms import InvoiceAdminForm
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.forms import ValidationError
from jalali_date import date2jalali, datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


class InvoiceItemInline(admin.TabularInline):
    # autocomplete_fields = ('product',)
    model = InvoiceItem
    extra = 1

    # prepopulated_fields = {'price': ['product.price', ]}


@admin.register(Invoice)
class InvoiceAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    form = InvoiceAdminForm
    inlines = (InvoiceItemInline,)
    list_display = ("__str__", 'date', 'link_to_invoice', 'get_created_jalali')
    search_fields = ('id',)
    autocomplete_fields = ('contact', 'company')

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.date).strftime('%y/%m/%d _ %H:%M:%S')

    def link_to_invoice(self, obj):
        return format_html('<a href="{}" target="_blank">Go to invoice</a>', reverse('invoice', args=(obj.id,)))

    link_to_invoice.short_description = 'link'
    get_created_jalali.short_description = 'تاریخ شمسی'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    exclude = ('slug',)
