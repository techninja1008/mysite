import datetime
import uuid
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page = models.CharField(max_length=100)

    def __str__(self):
        return self.page

    def get_absolute_url(self):
        return reverse('home:index', args=[self.page])

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    heading_text = models.CharField(max_length=200)
    body_text = models.TextField(max_length=600)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading_text

class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link_website = models.CharField(max_length=200)
    link_text = models.CharField(max_length=200)
    link_href = models.CharField(max_length=100)

    def __str__(self):
        return self.link_website

