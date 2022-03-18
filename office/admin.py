from django.contrib import admin
from .models import Letter, Hashtag, Employer
from jalali_date import date2jalali, datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'birthdate', 'partner',)
    search_fields = ('name_fa', 'lastname_fa', 'lastname_en', 'name_en',)
    list_filter = ('partner',)


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'to_contact', 'to_company',)
    search_fields = ('to_company', 'to_company',)
    list_filter = ('date',)
    autocomplete_fields = ('to_contact', 'to_company', 'hashtag', 'writer')


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name', 'slug',)
