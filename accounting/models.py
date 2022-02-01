from django.db import models
from django.contrib.auth.models import User
from contacts.models import Contact, Company

CURRENCY = [
    ('IRR', 'Rial'),
    ('USD', 'US Dollar'),
]


class SalaryManager(models.Manager):
    def salary(self):
        salary = self.get_queryset().filter(to__is_superuser=False)
        return salary


class PayManager(models.Manager):
    # returns pays base on employer and user is worker (not supersuer)
    # returns salaries of worker user
    # it will calculate the salaries of the worker
    def pay_employer_worker(self):
        users = User.objects.filter(is_superuser=False)
        pays = self.get_queryset().filter(source='employer', payer__is_superuser=False)
        salaries = Salary.objects.all()
        sals = []
        costs = []
        all_payments = []
        for user in users:
            for pay in pays:
                if user.id == pay.payer.id:
                    costs.append(int(pay.price))
                payments = {
                    'user': user.username,
                    'costs': costs,
                    'sum': sum(costs)
                }
            for salary in salaries:
                if user.id == salary.to.id:
                    sals.append(int(salary.price))
                payments['salaries'] = sals
                payments['salaries_sum'] = sum(sals)
                payments['calculate_salary'] = sum(sals) - sum(costs)
            all_payments.append(payments)
            sals = []
            costs = []
        return all_payments

    # returns pays base on employer source and partner (is_superuser)
    def pay_employer_partner(self):
        users = User.objects.filter(is_superuser=True)
        pays = self.get_queryset().filter(source='employer', payer__is_superuser=True)
        funds = Fund.objects.all()
        costs = []
        all_payments = []
        user_funds = []
        for user in users:
            for pay in pays:
                if user.id == pay.payer.id:
                    costs.append(int(pay.price))
                payments = {
                    'user': user.username,
                    'costs': costs,
                    'sum': sum(costs)
                }
            for fund in funds:
                if user.id == fund.user.id:
                    user_funds.append(int(fund.price))
                    payments['funds'] = user_funds
                    payments['funds_sum'] = sum(user_funds)
            all_payments.append(payments)
            costs = []
            user_funds = []
        return all_payments


class IncomeManager(models.Manager):
    def income_official_account(self):
        return self.get_queryset().filter(to_bank_account__is_official=True)

    def sum_income_official_account(self):
        incomes = self.get_queryset().filter(to_bank_account__is_official=True)
        list_of_income = []
        for i in incomes:
            list_of_income.append(int(i.price))
        return sum(list_of_income)


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
    # todo: employer (fetch form contact and companye : can you fetch both of them in one model?)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
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
    is_official = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Salary(models.Model):
    to = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default=False)
    price = models.CharField(max_length=32, null=False, blank=False)
    price_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0])
    bank_account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE, )
    date_of_payment = models.DateField(null=False, blank=False)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = SalaryManager()

    class Meta:
        verbose_name_plural = "Salaries"


class Income(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    price = models.CharField(max_length=32, null=False, blank=False)
    price_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0])
    to_bank_account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE, )
    from_contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE)
    from_company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    objects = IncomeManager()

    def __str__(self):
        return self.title


class Fund(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default=False)
    price = models.CharField(max_length=32, null=False, blank=False)
    price_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0])
    to_bank_account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE, )
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
    price = models.IntegerField(null=False, blank=False)
    price_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0])
    fee = models.CharField(max_length=32, null=True, blank=True)
    fe_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0])
    taxation = models.CharField(max_length=32, null=True, blank=True)
    taxation_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0])
    to = models.CharField(max_length=256, null=True, blank=False, help_text='Like Seven Host or Korosh Walmart')
    payer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default=False)
    # todo: study about on_delete
    source = models.CharField(max_length=32, choices=SOURCE, null=False, blank=False, default=SOURCE[0],
                              help_text='it means you spend money form your pocket or the company')
    account = models.ForeignKey(BankAccount, null=True, blank=True, on_delete=models.CASCADE, default=False)
    date_of_payment = models.DateField(null=False, blank=False)
    invoice = models.CharField(max_length=64, choices=INVOICE, null=False, blank=False,
                               default=(('no_invoice'), ('No Invoice')))
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2048, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PayManager()

    # todo: upload invoice
    # todo: add Shamsi date of payment
    # todo: add the payer - pardakht konandeh

    def __str__(self):
        return self.title
