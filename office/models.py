from django.contrib.auth.models import User
from django.db import models
from contacts.models import Contact, Company
from tinymce.models import HTMLField


class Hashtag(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True,
                            help_text='This Field Should be English')

    def __str__(self):
        return self.name


class Letter(models.Model):
    SEND = [
        ('email', 'Email'),
        ('fax', 'Fax'),
        ('post', 'Post'),
        ('delivery', 'Delivery'),
        ('employer', 'Employer')
    ]
    TYPE = [
        ('virtual', 'Virtual'),
        ('physical', 'Physical')
    ]
    to_contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE)
    to_company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=64, blank=False, null=False)
    subject = models.CharField(max_length=512, blank=False, null=False)
    date = models.DateField(null=False, blank=False)
    writer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # todo: do something to sing (Emza konnande)
    # sign = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    send_with = models.CharField(max_length=32, choices=SEND, null=True, blank=True, default=('delivery', 'Delivery'))
    type = models.CharField(max_length=32, choices=TYPE, null=True, blank=True, default=('physical', 'Physical'))
    content = HTMLField(null=False, blank=False)
    hashtag = models.ManyToManyField(Hashtag)
