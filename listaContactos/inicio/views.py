from django.shortcuts import render
from django.http import HttpResponse

def myHomeView(request, *args, **kwargs):
    myContext ={
        "myText":"Esto es sobre nosotros.",
        "myNumber": 123,
    }
    return render(request, "home.html", myContext)

#def about_view(request):
    #return render(request, 'about.html')