from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from answers.models import Resource
from .forms import ContributionForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def contribute(request):
    if request.method == 'POST':
        # creat a form that have request.POST data
        form = ContributionForm(request.POST)
        if form.is_valid():
            # the validated form data will be in
            # form.cleaned_data dictionary
            form.save()
            #topic = form.cleaned_data.get('topic')
            #introduce = form.cleaned_data.get('introduce')
            #location = form.cleaned_data.get('location')
            # the below one is a "flashed message"
            messages.success(request, f'您辛苦了, 我已经用小本本记下来了~')
            return redirect('/homepage')  # the 1st para in redirect is the name we gave to our URL patten
    else:
        # just create a blank form
        form = ContributionForm()
    return render(request, 'main_page/contribution.html', {'form': form})


def search_function(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        results = Resource.objects.filter(title__contains=search)
        return render(request,'main_page/results.html', {'results':results})
    else:
        return render(request,'main_page/welcome.html')




class ResourceListView(ListView):
    model = Resource
    template_name = 'main_page/welcome.html'
    context_object_name = 'resources'
    ordering = ['-date_posted']
    paginate_by =  5
