from django.urls import path
from . import views
urlpatterns = [
    path('praise/', views.praise,name='praise'),
    path('criticize/', views.criticize, name='criticize'),
]
