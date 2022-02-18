from django.contrib import admin
from .models import Comment, Post


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('content', 'is_published', 'added_date')
    readonly_fields = ('added_date',)
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (CommentInline,)
