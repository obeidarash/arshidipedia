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
class LetterAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('subject', 'to_contact', 'to_company', 'get_created_jalali')
    search_fields = ('to_company', 'to_company',)
    list_filter = ('date',)
    autocomplete_fields = ('to_contact', 'to_company', 'hashtag', 'writer')

    def get_created_jalali(self, obj):
        return date2jalali(obj.date).strftime('%y/%m/%d')

    get_created_jalali.short_description = "تاریخ"


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name', 'slug',)
