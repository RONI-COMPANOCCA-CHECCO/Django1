from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm, RawPersonaForm

def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
        "objeto": obj,
    }
    return render(request, "personas/test.html", context)

def personasAnotherCreateView(request):
    form = RawPersonaForm()
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    context ={
        "form": form,
    }
    return render(request, "personas/personasCreate.html", context)
def searchForHelp(request):
    return render(request, "personas/search.html", {})