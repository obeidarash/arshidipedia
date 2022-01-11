from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


class OfficialInvoices(models.Model):
    LOCATION = [
        ('company_office', 'Company Office'),
        ('employer_office', 'Employer Office'),
        ]
    STATUS = [
        ('current', 'Current'),
        ('invalid', 'Invalid'),
        ('lost', 'Lost'),
        ]
    # todo: employer (fetch form contact and companye)
    # todo: convert date of invoice to shamsi
    # todo: add date of create and update
    title = models.CharField(max_length=64, null=False, blank=False, unique=True)
    employer_signature = models.BooleanField(null=False, blank=False, default=False)
    location = models.CharField(max_length=64, choices=LOCATION, null=False, blank=False,
                               default=(('company_office'), ('Company Office')))
    status = models.CharField(max_length=64, choices=STATUS, null=False, blank=False,
                               default=(('current'), ('Current')))
    # This can be integer Field
    serial_number = models.CharField(max_length=32, null=False, blank=False)
    date_of_invoice = models.DateField(null=False, blank=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True)

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
    account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE, default=False)
    date_of_payment = models.DateField(null=False, blank=False)
    invoice = models.CharField(max_length=64, choices=INVOICE, null=False, blank=False,
                               default=(('no_invoice'), ('No Invoice')))
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2048, null=True, blank=True)

    # todo: upload invoice
    # todo: add Shamsi date of payment
    # todo: change price to price model you should search for it
    # todo: add the payer - pardakht konandeh
    # todo: add date of create and update

    def __str__(self):
        return self.title
