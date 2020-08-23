from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    topic = models.CharField(max_length=50)
    introduce = models.TextField(max_length=200)
    location = models.TextField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.topic

