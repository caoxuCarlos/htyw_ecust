from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from .forms import ContributionForm
from django.contrib import messages

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



class ResourceListView(ListView):
    model = Post
    template_name = 'main_page/welcome.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by =  3
