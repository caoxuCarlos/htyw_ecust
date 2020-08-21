from django import forms
from .models import Post


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['topic', 'introduce']
