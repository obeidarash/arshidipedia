from django.contrib import admin
from .models import Pay, Category, BankAccount, Income, OfficialInvoices, Salary, Fund
from .forms import IncomeAdminForm, OfficialInvoicesAdminForm
from django.http import HttpResponse
from jalali_date import date2jalali, datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
import csv


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    fields = [('price', 'price_currency'), 'user', 'account', 'comment']
    list_display = ('user', 'price',)
    search_fields = ('user',)


@admin.register(Salary)
class SalaryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('to', 'price', 'get_created_jalali')
    search_fields = ('to',)
    list_filter = ('to', 'bank_account', 'date')

    def get_created_jalali(self, obj):
        return date2jalali(obj.date).strftime('%y/%m/%d')

    get_created_jalali.short_description = "تاریخ"


@admin.register(OfficialInvoices)
class OfficialInvoicesAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    form = OfficialInvoicesAdminForm
    list_display = ('title', 'location', 'date_of_invoice', 'status', 'employer_signature', 'get_created_jalali')
    search_fields = ('title',)
    autocomplete_fields = ('contact', 'company',)

    # list_editable = ('employer_signature',)

    def get_created_jalali(self, obj):
        return date2jalali(obj.date_of_invoice).strftime('%y/%m/%d')

    get_created_jalali.short_description = "تاریخ"


@admin.register(Pay)
class PayAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    fields = ['title', ('price', 'price_currency'), ('fee', 'fee_currency'), ('taxation', 'taxation_currency'),
              ('account', 'to'), 'category', 'date', 'payer', 'source', 'invoice', 'attach', 'comment']
    list_display = ('title', 'category', 'price', 'source', 'get_created_jalali')
    search_fields = ('title', 'price',)
    autocomplete_fields = ('category',)
    list_filter = ['account', 'date', 'source']
    actions = ('export_as_csv',)

    def get_created_jalali(self, obj):
        return date2jalali(obj.date).strftime('%y/%m/%d')

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "گرفتن خروجی اکسل"
    get_created_jalali.short_description = "تاریخ شمسی"


@admin.register(Income)
class IncomeAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    form = IncomeAdminForm
    list_display = ('title', 'price', 'get_created_jalali')
    search_fields = ('title',)
    autocomplete_fields = ('contact', 'company', 'invoice',)
    list_filter = ('date', 'account')

    def get_created_jalali(self, obj):
        return date2jalali(obj.date).strftime('%y/%m/%d')

    get_created_jalali.short_description = "تاریخ شمسی"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('title', 'bank', 'is_official')
    search_fields = ('title',)
