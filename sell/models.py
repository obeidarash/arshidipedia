from django.db import models
from accounting.models import Contact, Company


class Invoice(models.Model):
    to_contact = models.ForeignKey(Contact, blank=False, null=False, on_delete=models.CASCADE)
    to_company = models.ForeignKey(Company, blank=False, null=False, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, verbose_name="تاریخ")


class Product(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    slug = models.SlugField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.name


class InvoiceItem(models.Model):
    UNIT = [
        ('Km', 'km'),
        ('Mile', 'mile')
    ]
    unit = models.CharField(choices=UNIT, max_length=128, blank=False, null=False, default=('Km', 'km'))
    Invoice = models.ForeignKey(Invoice, blank=False, null=False, on_delete=models.CASCADE)
    satellite = models.ForeignKey(Product, blank=False, null=False, on_delete=models.CASCADE)
    price = models.BigIntegerField(null=False, blank=False, verbose_name="مبلغ")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # todo: tedad
