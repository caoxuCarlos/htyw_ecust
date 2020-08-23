from django.db import models

# Create your models here.

class Suggestion(models.Model):
    topic = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    def __str__(self):
        return self.topic
