from django.contrib.auth.models import User
from django.db import models
from contacts.models import Contact, Company
from tinymce.models import HTMLField


class Employer(models.Model):
    name_fa = models.CharField(max_length=64, null=False, blank=False, verbose_name="نام به فارسی")
    lastname_fa = models.CharField(max_length=64, null=False, blank=False, verbose_name="نام خانوادگی به فارسی")
    name_en = models.CharField(max_length=64, null=False, blank=False, verbose_name="نام به انگلیسی")
    lastname_en = models.CharField(max_length=64, null=False, blank=False, verbose_name="نام خانوادگی به انگلیسی")
    national_code = models.CharField(max_length=32, null=True, blank=True, verbose_name='کد ملی')
    partner = models.BooleanField(default=False, verbose_name='شریک است؟')
    birthdate = models.DateField(null=True, blank=True, verbose_name='تاریخ تولد')

    class Meta:
        verbose_name_plural = 'کارمند'
        verbose_name = 'کارمند'
        unique_together = ('national_code',)
        ordering = ['-lastname_fa']

    def __str__(self):
        return self.name_fa + " " + self.lastname_fa


class Hashtag(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True, verbose_name="نام")
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True,
                            help_text='به انگلیسی و مختصر باشد به جای اسپیس از خط تیره استفاده شود',
                            verbose_name="اسلاگ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = "برچسب"


class Letter(models.Model):
    SEND = [
        ('email', 'ایمیل'),
        ('fax', 'فکس'),
        ('post', 'پست'),
        ('delivery', 'پیک'),
        ('employer', 'کارمند')
    ]
    TYPE = [
        ('virtual', 'مجازی (پی دی اف)'),
        ('physical', 'فیزیکی')
    ]
    to_contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE, verbose_name="به مخاطب")
    to_company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE, verbose_name="به شرکت")
    number = models.CharField(max_length=64, blank=False, null=False, verbose_name="شماره")
    subject = models.CharField(max_length=512, blank=False, null=False, verbose_name="موضوع")
    date = models.DateField(null=False, blank=False, verbose_name="تاریخ")
    writer = models.ForeignKey(Employer, null=True, blank=True, on_delete=models.CASCADE, verbose_name="نویسنده")
    # todo: do something to sing (Emza konnande)
    # sign = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    send_with = models.CharField(max_length=32, choices=SEND, null=True, blank=True, default=('delivery', 'پیک'),
                                 verbose_name="نحوه ارسال")
    type = models.CharField(max_length=32, choices=TYPE, null=True, blank=True, default=('physical', 'فیزیکی'),
                            verbose_name="نوع نامه")
    content = HTMLField(null=False, blank=False, verbose_name="متن نامه")
    hashtag = models.ManyToManyField(Hashtag, verbose_name="برچسب", blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'نامه'
        verbose_name_plural = "نامه"
