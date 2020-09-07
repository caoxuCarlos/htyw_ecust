from django.urls import path
from . import views
urlpatterns = [
    path('', views.slide, name='slide-first'),
    path('service1', views.making, name='service1'),
    path('service2', views.modification, name='service2'),
]
