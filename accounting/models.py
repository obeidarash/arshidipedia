from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.title


class BankAccount(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    bank = models.CharField(max_length=256, null=False, blank=False)
    card = models.CharField(max_length=256, null=False, blank=False)
    shomare_hesab = models.CharField(max_length=256, null=False, blank=False)
    shaba = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.title


class Pay(models.Model):
    INVOICE = [
        ('no_invoice', 'No Invoice'),
        ('invoice', 'Invoice'),
        ('official_invoice', 'Official Invoice'),
    ]
    title = models.CharField(max_length=256, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False, help_text='It should be in Rial')
    fee = models.IntegerField(null=True, blank=True)
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
