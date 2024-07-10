from django.shortcuts import render

def myHomeView(request, *args, **kwargs):
    myContext = {
        "myText": "Esto es sobre nosotros.",
        "myNumber": 123,
        "myList": [33, 44, 55],
    }
    return render(request, "home.html", myContext)

def myNamesView(request, *args, **kwargs):
    myContext = {
        "myText": "Lista de nombres.",
        "myNumber": 456,
        "nombres": ["Alice", "Bob", "Charlie"],
    }
    return render(request, "names.html", myContext)

#def about_view(request):
    #return render(request, 'about.html')