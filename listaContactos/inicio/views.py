from django.shortcuts import render
from django.http import HttpResponse

def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html")

def about_view(request):
    return render(request, 'about.html')