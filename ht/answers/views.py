from django.shortcuts import render
from django.views.generic import ListView
from .models import Resource

# Create your views here.
class ResourceListView(ListView):
    model = Resource
    template_name = 'answers/answer_page.html'
    context_object_name = 'resources'
    ordering = ['-date_posted']
    paginate_by = 8
