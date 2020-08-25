"""ht URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from answers import views as answers_view
from main_page import views as main_page_view
from money_job import views as money_job_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('homepage/', include('main_page.urls')),
    # hijack homepage url to answers page (prevent unauthorized bad information)
    path('homepage/', answers_view.ResourceListView.as_view(), name='home'),
    path('tip/', include('tip.urls')),
    path('answers/', answers_view.ResourceListView.as_view(), name='answers'),
    path('contribute/', main_page_view.contribute, name='contribute'),
    path('jobs/', money_job_view.JobListView.as_view(), name='jobs'),
    path('job_submit/', money_job_view.submit_job, name='job_submit'),
]

