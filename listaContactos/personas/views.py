from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
        "objeto": obj,
    }
    return render(request, "personas/test.html", context)

def personaCreateView(request):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonaForm()  
    else:
        print(form.errors)  

    context = {
        "form": form
    }
    return render(request, "personas/personasCreate.html", context)

def searchForHelp(request):
    return render(request, "personas/search.html", {})