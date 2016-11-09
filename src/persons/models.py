from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Allowed format: '+000000000'. Up to 15 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=250)

    class Meta:
        ordering = ['timestamp']

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} {}'.format(self.name, self.last_name)
