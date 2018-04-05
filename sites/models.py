from django.db import models
from django.urls import reverse


class Site(models.Model):
    short_name = models.CharField(max_length=200)
    reference = models.CharField(max_length=200)

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse(self.reference)
# Create your models here.
