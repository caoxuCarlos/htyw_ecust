from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    topic = models.CharField(max_length=50)
    introduce = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.topic

