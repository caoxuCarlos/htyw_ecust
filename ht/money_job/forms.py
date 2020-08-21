from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['subject', 'how_much', 'job_detail','deadline','contact','post_date']