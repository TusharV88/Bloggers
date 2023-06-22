from django.utils import timezone
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateField(default=timezone.now)
