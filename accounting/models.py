from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from contacts.models import Contact, Company


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class BankAccount(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    bank = models.CharField(max_length=256, null=False, blank=False)
    card_number = models.CharField(max_length=256, null=False, blank=False, unique=True)
    account_number = models.CharField(max_length=256, null=False, blank=False, unique=True)
    shaba = models.CharField(max_length=256, null=False, blank=False, unique=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Received(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    price = MoneyField(max_digits=14, decimal_places=0, default_currency='IRR', null=False, blank=False)
    bank_account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE,)
    from_contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE)
    from_company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)


class Pay(models.Model):
    INVOICE = [
        ('no_invoice', 'No Invoice'),
        ('invoice', 'Invoice'),
        ('official_invoice', 'Official Invoice'),
    ]
    title = models.CharField(max_length=256, null=False, blank=False)
    price = MoneyField(max_digits=14, decimal_places=0, default_currency='IRR', null=False, blank=False)
    fee = MoneyField(max_digits=14, decimal_places=0, default_currency='IRR', null=True, blank=True)
    taxation = MoneyField(max_digits=14, decimal_places=0, default_currency='IRR', null=True, blank=True,
                          help_text='Taxation and VAT')
    to = models.CharField(max_length=256, null=True, blank=False, help_text='Like Seven Host or Korosh Walmart')
    payer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default=False)
    # todo: study about on_delete
    account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE, default=False)
    date_of_payment = models.DateField(null=False, blank=False)
    invoice = models.CharField(max_length=64, choices=INVOICE, null=False, blank=False,
                               default=(('no_invoice'), ('No Invoice')))
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2048, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # todo: upload invoice
    # todo: add Shamsi date of payment
    # todo: add the payer - pardakht konandeh

    def __str__(self):
        return self.title
