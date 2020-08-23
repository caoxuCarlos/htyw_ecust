from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import Job
from .forms import JobForm
# Create your views here.
def submit_job(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JobForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            #topic = form.cleaned_data.get('topic')
            #introduce = form.cleaned_data.get('introduce')
            #location = form.cleaned_data.get('location')
            # the below one is a "flashed message"
            messages.success(request, f'得嘞客官, 您的任务已经成功发布!')
            return redirect('/jobs')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = JobForm()

    return render(request, 'money_job/job_submit.html', {'form': form})

class JobListView(ListView):
    model = Job
    template_name = 'money_job/job_page.html'
    context_object_name = 'jobs'
    ordering = ['-post_date']
    paginate_by = 5
