from django.db import models
from accounting.models import Contact, Company


class Invoice(models.Model):
    to_contact = models.ForeignKey(Contact, blank=False, null=False, on_delete=models.CASCADE)
    to_company = models.ForeignKey(Company, blank=False, null=False, on_delete=models.CASCADE)


class Satellite(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True)


class InvoiceItem(models.Model):
    Invoice = models.ForeignKey(Invoice, blank=False, null=False, on_delete=models.CASCADE)
    satellite = models.ForeignKey(Satellite, blank=False, null=False, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=52, blank=True, null=True)


class Comment(models.Model):
    blog = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    added_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

    def __str__(self):
        return f"{self.blog.title} - {self.content}"
