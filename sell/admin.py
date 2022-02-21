from django.contrib import admin
from .models import Comment, Post, InvoiceItem, Invoice, Product


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1


@admin.register(Invoice)
class PostAdmin(admin.ModelAdmin):
    inlines = (InvoiceItemInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('content', 'is_published', 'added_date')
    readonly_fields = ('added_date',)
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (CommentInline,)
