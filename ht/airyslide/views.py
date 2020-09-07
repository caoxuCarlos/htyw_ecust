from django.shortcuts import render

# Create your views here.
def slide(request):
    return render(request,'airyslide/first-page.html')

def making(request):
    return render(request,'airyslide/service1.html')

def modification(request):
    return render(request,'airyslide/service2.html')
