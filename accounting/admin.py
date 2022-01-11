from django.contrib import admin
from .models import Pay, Category, BankAccount, Received


@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('title', 'payer', 'category', 'price',)
    search_fields = ('title', 'price',)
    autocomplete_fields = ('category',)
    list_filter = ['payer', 'account', 'date_of_payment']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Received)
class ReceivedAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('title', 'bank')
    search_fields = ('title',)
