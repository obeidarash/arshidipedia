from django.contrib import admin
from .models import Letter, Hashtag, Employer


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'birthdate',)
    search_fields = ('name_fa', 'lastname_fa', 'lastname_en', 'name_en',)


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'to_contact', 'to_company',)
    search_fields = ('to_company', 'to_company',)
    list_filter = ('date',)
    autocomplete_fields = ('to_contact', 'to_company', 'hashtag')


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name', 'slug',)
