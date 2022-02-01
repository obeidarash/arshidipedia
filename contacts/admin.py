from django.contrib import admin
from .models import Contact, Company, Address, Hashtag


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    # prepopulated_fields = {"slug": ("name",)}


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('title', 'address',)
    search_fields = ('title', 'address',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name_fa', 'name_en',)
    search_fields = ('name_fa', 'name_en',)
    autocomplete_fields = ('contact', 'hashtag')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name_fa', 'lastname_fa', 'gender',)
    search_fields = ('name_fa', 'lastname_fa',)
    autocomplete_fields = ('hashtag',)
