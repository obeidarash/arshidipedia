from django.db import models
from accounting.models import Contact, Company
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Invoice(models.Model):
    contact = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.CASCADE, verbose_name='مخاطب')
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, verbose_name='شرکت')
    date = models.DateField(null=False, blank=False, verbose_name="تاریخ")
    is_cancel = models.BooleanField(default=False, verbose_name='لغو شده؟')
    description = models.TextField(max_length=2048, null=True, blank=True, verbose_name='توضیحات')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'پیش فاکتور'
        verbose_name_plural = 'پیش فاکتور'

    def __str__(self):
        if self.contact:
            return self.contact.name_fa + "-" + str(self.id)
        elif self.company:
            return self.company.name_fa + "-" + str(self.id)
        return str(self.date) + " " + str(self.created)


class Product(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='نام')
    price = models.BigIntegerField(null=False, blank=False, verbose_name='قیمت')
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True)
    unit = models.CharField(max_length=128, blank=False, null=False, verbose_name='واحد')
    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'
    def __str__(self):
        return self.name

class InvoiceItem(models.Model):
    product = models.ForeignKey(Product, blank=False, null=False, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.IntegerField(null=False, blank=False, verbose_name='مقدار')
    price = models.BigIntegerField(null=False, blank=False, verbose_name='قیمت')
    Invoice = models.ForeignKey(Invoice, blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'آیتم های فاکتور'
        verbose_name_plural = 'آیتم های فاکتور'

    def __str__(self):
        return self.product.name
