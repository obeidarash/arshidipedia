from django.db import models
from accounting.models import Contact, Company


class Sell(models.Model):
    # todo: you can connect to the incomes
    to_user = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE)
    to_company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
