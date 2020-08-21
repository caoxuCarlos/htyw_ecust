from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Job(models.Model):
    subject = models.TextField()
    how_much = models.DecimalField(decimal_places=2,max_digits=6)
    job_detail = models.TextField()
    deadline = models.TextField()
    contact = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.subject
