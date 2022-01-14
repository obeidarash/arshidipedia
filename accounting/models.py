from django.db import models
from django.contrib.auth.models import User
from contacts.models import Contact, Company

CURRENCY = [
    ('IRR', 'Rial'),
    ('USD', 'US Dollar'),
]


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
    title = models.CharField(max_length=64, null=False, blank=False, unique=True)
    location = models.CharField(max_length=64, choices=LOCATION, null=False, blank=False,
                                default=(('company_office'), ('Company Office')))
    status = models.CharField(max_length=64, choices=STATUS, null=False, blank=False,
                              default=(('current'), ('Current')))
    # This can be integer Field
    serial_number = models.CharField(max_length=32, null=False, blank=False)
    date_of_invoice = models.DateField(null=False, blank=False)
    employer_signature = models.BooleanField(null=False, blank=False, default=False)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


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


class Salary(models.Model):
    to = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default=False)
    price = models.CharField(max_length=32, null=False, blank=False)
    bank_account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE, )
    date_of_payment = models.DateField(null=False, blank=False)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Salaries"


class Received(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    price = models.CharField(max_length=32, null=False, blank=False)
    to_bank_account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE, )
    from_contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE)
    from_company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)


class Pay(models.Model):
    INVOICE = [
        ('no_invoice', 'No Invoice'),
        ('invoice', 'Invoice'),
        ('official_invoice', 'Official Invoice'),
    ]
    SOURCE = [
        ('employer', 'Employer'),
        ('company', 'Company')
    ]
    title = models.CharField(max_length=256, null=False, blank=False)
    price = models.CharField(max_length=32, null=False, blank=False)
    price_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0])
    fee = models.CharField(max_length=32, null=True, blank=True)
    fe_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0])
    taxation = models.CharField(max_length=32, null=True, blank=True)
    taxation_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0])
    to = models.CharField(max_length=256, null=True, blank=False, help_text='Like Seven Host or Korosh Walmart')
    payer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default=False)
    # todo: study about on_delete
    source = models.CharField(max_length=32, choices=SOURCE, null=False, blank=False, default=SOURCE[0])
    # todo: account can be optional
    account = models.ForeignKey(BankAccount, null=True, blank=True, on_delete=models.CASCADE, default=False)
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
