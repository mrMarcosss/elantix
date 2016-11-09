from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE

from persons.models import Person


class Review(models.Model):
    author = models.ForeignKey(Person)
    person = models.ForeignKey(Person, related_name='reviews', db_index=True, on_delete=CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} to - {}'.format(self.author.get_full_name(), self.person.get_full_name())
