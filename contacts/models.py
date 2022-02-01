from django.db import models
from django_countries.fields import CountryField
from django.core.validators import EmailValidator, URLValidator


class Hashtag(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True,
                            help_text='This Field Should be English')

    def __str__(self):
        return self.name


class Address(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    country = CountryField(blank_label='select country', null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    province = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    plate = models.IntegerField(null=True, blank=True)
    zipcode = models.CharField(max_length=32, null=True, blank=True)


class Contact(models.Model):
    GENDER = (('mr', 'Mr'), ('ms', 'Ms'))
    name_fa = models.CharField(max_length=64, null=True, blank=True)
    lastname_fa = models.CharField(max_length=64, null=False, blank=False)
    name_en = models.CharField(max_length=64, null=True, blank=True)
    lastname_en = models.CharField(max_length=64, null=True, blank=True)
    gender = models.CharField(max_length=16, choices=GENDER, null=False, blank=False)
    position = models.CharField(max_length=64, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, help_text="Seperate emails with comma",
                              validators=(EmailValidator,))
    telephone = models.CharField(max_length=32, null=True, blank=True)
    mobile_1 = models.CharField(max_length=32, null=True, blank=True)
    mobile_2 = models.CharField(max_length=32, null=True, blank=True)
    website = models.URLField(max_length=512, null=True, blank=True, validators=[URLValidator, ])
    national_code = models.CharField(max_length=32, null=True, blank=True)
    hashtag = models.ManyToManyField(Hashtag, null=True, blank=True)
    comment = models.TextField(max_length=2048, null=True, blank=True)

    # todo: add email in here
    # todo: add validator to the tables

    def __str__(self):
        if self.name_fa:
            return self.name_fa + " " + self.lastname_fa
        return self.lastname_fa


class Company(models.Model):
    name_fa = models.CharField(max_length=128, null=True, blank=True)
    name_en = models.CharField(max_length=128, null=True, blank=True)
    website = models.URLField(max_length=512, null=True, blank=True, validators=[URLValidator, ])
    telephone = models.CharField(max_length=32, null=True, blank=True)
    economic_code = models.CharField(max_length=16, null=True, blank=True)
    national_id = models.CharField(max_length=16, null=True, blank=True)
    workshop_code = models.CharField(max_length=16, null=True, blank=True)
    registration_number = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, help_text="Seperate emails with comma",
                              validators=(EmailValidator,))
    contact = models.ManyToManyField(Contact, blank=True, verbose_name="Employee(s)")
    hashtag = models.ManyToManyField(Hashtag, null=True, blank=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = "Companies"

    def __str__(self):
        if self.name_fa and self.name_en:
            return self.name_fa + ' / ' + self.name_en
        if self.name_fa:
            return self.name_fa
        if self.name_en:
            return self.name_en
        return "No name!"
