from django.db import models
from django_countries.fields import CountryField
from django.core.validators import EmailValidator, URLValidator


class Hashtag(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True, verbose_name="نام برچسب")
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True,
                            help_text='به انگلیسی باشد، به جای اسپیس از خط تیره استفاده کنید، هر چه کوتاه تر بهتر و با نام برچسب مرتبط باشد',
                            verbose_name="اسلاگ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = "برچسب"


class Address(models.Model):
    ADDRESS = [('private', 'آدرس خصوصی یا شخصی'),
               ('invoice', 'آدرس فاکتور'),
               ('delivery ', 'آدرس ارسال یا دریافت'),
               ('other', 'دیگر آدرس ها ')]
    title = models.CharField(max_length=256, null=False, blank=False, verbose_name="نام آدرس")
    type = models.CharField(max_length=128, choices=ADDRESS, null=False, blank=True,
                            default=('delivery ', 'Delivery Address'), verbose_name="نوع آدرس")
    country = CountryField(blank_label='select country', null=True, blank=True, verbose_name="کشور")
    city = models.CharField(max_length=64, null=True, blank=True, verbose_name="شهر")
    province = models.CharField(max_length=64, null=True, blank=True, verbose_name="شهرستان")
    address = models.CharField(max_length=512, null=True, blank=True, verbose_name="آدرس")
    plate = models.IntegerField(null=True, blank=True, verbose_name="پلاک")
    zipcode = models.CharField(max_length=32, null=True, blank=True, verbose_name="کد پستی")

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = "آدرس"


class Contact(models.Model):
    GENDER = (('mr', 'آقا'), ('ms', 'خانم'))
    name_fa = models.CharField(max_length=64, null=True, blank=True, verbose_name="نام به فارسی")
    lastname_fa = models.CharField(max_length=64, null=False, blank=False, verbose_name="نام خانوادگی به انگلیسی")
    name_en = models.CharField(max_length=64, null=True, blank=True, verbose_name="نام به انگلیسی")
    lastname_en = models.CharField(max_length=64, null=True, blank=True, verbose_name="نام خانوادگی به انگلیسی")
    gender = models.CharField(max_length=16, choices=GENDER, null=False, blank=False, verbose_name="جنسیت")
    position = models.CharField(max_length=64, null=True, blank=True, verbose_name="سمت")
    birthday = models.DateField(null=True, blank=True, verbose_name="تاریخ تولد")
    email = models.EmailField(null=True, blank=True, help_text="ایمیل ها را با کاما جدا کنید",
                              validators=(EmailValidator,), verbose_name="ایمیل (ها)")
    telephone = models.CharField(max_length=32, null=True, blank=True, verbose_name="تلفن")
    mobile_1 = models.CharField(max_length=32, null=True, blank=True, verbose_name="موبایل 1")
    mobile_2 = models.CharField(max_length=32, null=True, blank=True, verbose_name="موبایل 2")
    website = models.URLField(max_length=512, null=True, blank=True, validators=[URLValidator, ],
                              verbose_name="وب سایت")
    national_code = models.CharField(max_length=32, null=True, blank=True, verbose_name="کد ملی")
    hashtag = models.ManyToManyField(Hashtag, verbose_name="برچسب")
    comment = models.TextField(max_length=2048, null=True, blank=True, verbose_name="توضیحات")

    # todo: add email in here
    # todo: add validator to the tables

    def __str__(self):
        if self.name_fa:
            return self.name_fa + " " + self.lastname_fa
        return self.lastname_fa

    class Meta:
        verbose_name = 'مخاطب'
        verbose_name_plural = "مخاطب"


class Company(models.Model):
    name_fa = models.CharField(max_length=128, null=True, blank=True, verbose_name="نام شرکت به فارسی")
    name_en = models.CharField(max_length=128, null=True, blank=True, verbose_name="نام شرکت به انگلیسی")
    website = models.URLField(max_length=512, null=True, blank=True, validators=[URLValidator, ],
                              verbose_name="وب سایت")
    telephone = models.CharField(max_length=32, null=True, blank=True, verbose_name="تلفن")
    economic_code = models.CharField(max_length=16, null=True, blank=True, verbose_name="شماره اقتصادی")
    national_id = models.CharField(max_length=16, null=True, blank=True, verbose_name="شناسه ملی")
    workshop_code = models.CharField(max_length=16, null=True, blank=True, verbose_name="کد کارگاه")
    registration_number = models.CharField(max_length=16, null=True, blank=True, verbose_name="شماره ثبت")
    email = models.EmailField(null=True, blank=True, help_text="ایمیل ها را با کاما از هم جدا کنید",
                              validators=(EmailValidator,), verbose_name="ایمیل (ها)")
    contact = models.ManyToManyField(Contact, blank=True, verbose_name="کارمند (ها)")
    hashtag = models.ManyToManyField(Hashtag, verbose_name="برچسب")

    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = "شرکت"

    def __str__(self):
        if self.name_fa and self.name_en:
            return self.name_fa + ' / ' + self.name_en
        if self.name_fa:
            return self.name_fa
        if self.name_en:
            return self.name_en
        return "No name!"
