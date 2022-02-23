from django.contrib import admin
from .models import Pay, Category, BankAccount, Income, OfficialInvoices, Salary, Fund
from .forms import IncomeAdminForm


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ('user', 'price')
    search_fields = ('user',)


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('to', 'price')
    search_fields = ('to',)


@admin.register(OfficialInvoices)
class OfficialInvoicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date_of_invoice', 'status', 'employer_signature')
    search_fields = ('title',)
    # list_editable = ('employer_signature',)


@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'source',)
    search_fields = ('title', 'price',)
    autocomplete_fields = ('category',)
    list_filter = ['account', 'date_of_payment', 'source']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    form = IncomeAdminForm
    list_display = ('title', 'price')
    search_fields = ('title',)
    autocomplete_fields = ('contact', 'company', 'invoice',)


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('title', 'bank', 'is_official')
    search_fields = ('title',)
