from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Resource(models.Model):
    title = models.CharField(max_length=50)
    introduce = models.TextField()
    location = models.TextField()
    key = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    #def get_absolute_url(self):
    #    return reverse('resouce-detail', kwargs={'pk': self.pk})


