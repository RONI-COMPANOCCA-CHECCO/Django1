from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm, RawPersonaForm

def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
        "objeto": obj,
    }
    return render(request, "personas/test.html", context)

def personaCreateView(request):
    form = RawPersonaForm()
    context ={
        "form": form,
    }
    return render(request, "personas/personasCreate.html", context)
def searchForHelp(request):
    return render(request, "personas/search.html", {})