from django.shortcuts import render, redirect
from .forms import SuggestionForm
from django.contrib import messages

# Create your views here.

def praise(request):
    return render(request, 'tip/praise.html')

def criticize(request):
    if request.method == 'POST':
        # creat a form that have request.POST data
        form = SuggestionForm(request.POST)
        if form.is_valid():
            # the validated form data will be in
            # form.cleaned_data dictionary
            form.save()
            #topic = form.cleaned_data.get('topic')
            #introduce = form.cleaned_data.get('introduce')
            #location = form.cleaned_data.get('location')
            # the below one is a "flashed message"
            messages.success(request, f'已经提交成功, 非常感谢您的建议  \ (•◡•) /')
            return redirect('/homepage')  # the 1st para in redirect is the name we gave to our URL patten
    else:
        # just create a blank form
        form = SuggestionForm()
    return render(request, 'tip/criticize.html', {'form': form})
