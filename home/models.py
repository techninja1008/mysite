import datetime
import uuid
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Details(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    welcome_msg = models.TextField(max_length=600)

    def __str__(self):
        return self.welcome_msg[:10]
