import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

# Create your models here.
