from django.db import models


class PayAttach(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    file = models.FileField(upload_to='pay')
