from django.db import models
from django_countries.fields import CountryField


class Contact(models.Model):
    GENDER = (('mr', 'Mr'), ('ms', 'Ms'))
    name_fa = models.CharField(max_length=64, null=True, blank=True)
    lastname_fa = models.CharField(max_length=64, null=False, blank=False)
    name_en = models.CharField(max_length=64, null=True, blank=True)
    lastname_en = models.CharField(max_length=64, null=True, blank=True)
    gender = models.CharField(max_length=16, choices=GENDER, null=False, blank=False)
    telephone = models.CharField(max_length=32, null=True, blank=True)
    mobile_1 = models.CharField(max_length=32, null=True, blank=True)
    mobile_2 = models.CharField(max_length=32, null=True, blank=True)
    position = models.CharField(max_length=64, null=True, blank=True)
    national_code = models.CharField(max_length=32, null=True, blank=True)

    # todo: add company and email

    # Address
    country = CountryField(blank_label='select country', null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    province = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    plate = models.IntegerField(null=True, blank=True)
    zipcode = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        if self.name_fa:
            return self.name_fa + " " + self.lastname_fa
        return self.lastname_fa
