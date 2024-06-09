from django.shortcuts import render, request
from django.http import HttpResponse
# Create your views here.
def myHomeView(*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render("home.html")

def anotherView(request):
    return HttpResponse("<h1>Solo otra pagina</h1>")