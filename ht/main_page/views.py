from django.shortcuts import render
from .models import Post

# Create your views here.

def welcome(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main_page/welcome.html', context)