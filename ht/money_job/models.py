from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Job(models.Model):
    subject = models.CharField(max_length= 15)
    how_much = models.DecimalField(decimal_places=2,max_digits=6)
    job_detail = models.TextField(max_length= 500)
    deadline = models.CharField(max_length= 50)
    contact = models.CharField(max_length= 45)
    post_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.subject
