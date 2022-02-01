from django.contrib import admin
from .models import Letter, Hashtag


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
