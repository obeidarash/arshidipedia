import os
from django.db import models
from django.contrib.auth.models import User
from contacts.models import Contact, Company
from django.dispatch import receiver
import uuid

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
    # def pay_employer_worker(self):
    #     users = User.objects.filter(is_superuser=False)
    #     pays = self.get_queryset().filter(source='employer', payer__is_superuser=False)
    #     salaries = Salary.objects.all()
    #     sals = []
    #     costs = []
    #     all_payments = []
    #     for user in users:
    #         for pay in pays:
    #             if user.id == pay.payer.id:
    #                 costs.append(int(pay.price))
    #             payments = {
    #                 'user': user.username,
    #                 'costs': costs,
    #                 'sum': sum(costs)
    #             }
    #         for salary in salaries:
    #             if user.id == salary.to.id:
    #                 sals.append(int(salary.price))
    #             payments['salaries'] = sals
    #             payments['salaries_sum'] = sum(sals)
    #             payments['calculate_salary'] = sum(sals) - sum(costs)
    #         all_payments.append(payments)
    #         sals = []
    #         costs = []
    #     return all_payments

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
        ('company_office', 'شرکت'),
        ('employer_office', 'شرکت کارفرما'),
    ]
    STATUS = [
        ('current', 'جاری'),
        ('invalid', 'باطل'),
        ('lost', 'گمشده'),
    ]
    # todo: employer (fetch form contact and companye : can you fetch both of them in one model?)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE, verbose_name="شخص")
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE, verbose_name="شرکت")
    # todo: convert date of invoice to shamsi
    title = models.CharField(max_length=64, null=False, blank=False, unique=True, verbose_name="موضوع فاکتور")
    location = models.CharField(max_length=64, choices=LOCATION, null=False, blank=False,
                                default=(('company_office'), ('Company Office')), verbose_name="مکان فاکتور")
    status = models.CharField(max_length=64, choices=STATUS, null=False, blank=False,
                              default=(('current'), ('Current')), verbose_name="وضعیت فاکتور")
    # This can be integer Field
    serial_number = models.CharField(max_length=32, null=False, blank=False, verbose_name="شماره سریال فاکتور")
    date_of_invoice = models.DateField(null=False, blank=False, verbose_name="تاریخ فاکتور")
    employer_signature = models.BooleanField(null=False, blank=False, default=False, verbose_name="امضای کارفرما دارد؟")
    comment = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'فاکتور رسمی'
        verbose_name_plural = "فاکتور ها رسمی"

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False, unique=True, verbose_name="دسته بندی")
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True,
                            help_text='به انگلیسی باشد، هر چه کوتاه تر بهتر، به جای اسپیس از خط تیره استفاده کنید',
                            verbose_name="اسلاگ")

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title


class BankAccount(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False, verbose_name="توضیح")
    bank = models.CharField(max_length=256, null=False, blank=False, verbose_name="نام بانک")
    card_number = models.CharField(max_length=256, null=False, blank=False, unique=True, verbose_name="شماره کارت")
    account_number = models.CharField(max_length=256, null=False, blank=False, unique=True, verbose_name="شماره حساب")
    shaba = models.CharField(max_length=256, null=False, blank=False, unique=True, verbose_name="شبا")
    is_official = models.BooleanField(default=False, verbose_name="حساب رسمی است؟")
    comment = models.TextField(null=True, blank=True, verbose_name="توضیحات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'حساب بانکی'
        verbose_name_plural = "حساب های بانکی"


class Salary(models.Model):
    to = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default=False,
                           verbose_name="به حساب کارمند")
    price = models.CharField(max_length=32, null=False, blank=False, verbose_name="مبلغ")
    price_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0],
                                      verbose_name="واحد پول مبلغ")
    bank_account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE,
                                     verbose_name="از حساب بانکی")
    date_of_payment = models.DateField(null=False, blank=False, verbose_name="تاریخ پرداخت")
    comment = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = SalaryManager()

    class Meta:
        verbose_name = 'تنخواه'
        verbose_name_plural = "تنخواه ها"


class Income(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False, verbose_name="موضوع")
    price = models.CharField(max_length=32, null=False, blank=False, verbose_name="مبلغ")
    price_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0],
                                      verbose_name="واحد پول دریافتی")
    to_bank_account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE,
                                        verbose_name="به حساب بانکی")
    from_contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE, verbose_name="شخص")
    from_company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE, verbose_name="شرکت")
    comment = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    objects = IncomeManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دریافت'
        verbose_name_plural = "دریافتی ها"


class Fund(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default=False,
                             help_text="کارمندی را انتخاب کنید که در شرکت شریک است",
                             verbose_name="شریک")
    price = models.CharField(max_length=32, null=False, blank=False, verbose_name="هزینه")
    price_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0],
                                      verbose_name="واحد پول هزینه")
    to_bank_account = models.ForeignKey(BankAccount, null=False, blank=False, on_delete=models.CASCADE,
                                        verbose_name="به حساب بانکی")
    comment = models.TextField(null=True, blank=True, verbose_name="توضیحات")

    class Meta:
        verbose_name = 'سرمایه'
        verbose_name_plural = "سرمایه ها"


class Pay(models.Model):
    INVOICE = [
        ('no_invoice', 'بدون فاکتور'),
        ('invoice', 'فاکتور دارد'),
        ('official_invoice', 'فاکتور رسمی'),
    ]
    SOURCE = [
        ('employer', 'کارمند'),
        ('company', 'شرکت')
    ]
    title = models.CharField(max_length=256, null=False, blank=False, verbose_name="موضوع")
    price = models.IntegerField(null=False, blank=False, verbose_name="مقدار هزینه")
    price_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0],
                                      verbose_name="واحد پول")
    fee = models.CharField(max_length=32, null=True, blank=True, verbose_name="کارمزد")
    fe_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0],
                                   verbose_name="واحد پول کارمزد")
    taxation = models.CharField(max_length=32, null=True, blank=True, verbose_name="مالیات")
    taxation_currency = models.CharField(max_length=32, choices=CURRENCY, null=False, blank=True, default=CURRENCY[0],
                                         verbose_name="واحد پول مالیات")
    to = models.CharField(max_length=256, null=True, blank=False, help_text='Like Seven Host or Korosh Walmart',
                          verbose_name="به حساب")
    payer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default=False,
                              verbose_name="پرداخت کننده")
    # todo: study about on_delete
    source = models.CharField(max_length=32, choices=SOURCE, null=False, blank=False, default=SOURCE[0],
                              help_text='it means you spend money form your pocket or the company',
                              verbose_name="منبع پرداخت")
    account = models.ForeignKey(BankAccount, null=True, blank=True, on_delete=models.CASCADE, default=False,
                                verbose_name="حساب بانکی")
    date_of_payment = models.DateField(null=False, blank=False, verbose_name="تاریخ پرداخت")
    invoice = models.CharField(max_length=64, choices=INVOICE, null=False, blank=False,
                               default=(('no_invoice'), ('No Invoice')), verbose_name="وضعیت فاکتور")
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE, verbose_name="دسته بندی")
    attach = models.FileField(upload_to='pay', blank=True, null=True, verbose_name="پیوست")
    comment = models.TextField(max_length=2048, null=True, blank=True, verbose_name="توضیحات")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PayManager()

    # todo: upload invoice
    # todo: add Shamsi date of payment
    # todo: add the payer - pardakht konandeh

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = "پرداخت ها"
