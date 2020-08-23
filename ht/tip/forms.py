from django import forms
from django.forms import Textarea

from .models import Suggestion

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['topic','content']
        widgets = {
            'topic':forms.TextInput(attrs={
                'placeholder':'',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': '',
                'cols': '40',
                'rows': '5',
            }),
        }
        labels = {
            'topic': ('需要改进的方面:'),
            'content': ('具体内容:'),
        }
        help_texts = {
            'topic': ('   '),
            'content': ('   '),
        }
