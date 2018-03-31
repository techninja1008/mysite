import uuid
import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
from mysite import settings

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    created_date = models.DateTimeField('date created', default=timezone.now)
    published_date = models.DateTimeField('date published', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])
