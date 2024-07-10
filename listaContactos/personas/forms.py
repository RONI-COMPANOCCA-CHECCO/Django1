from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'edad', 'donador']

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad <= 0:
            raise forms.ValidationError("La edad debe ser un número positivo.")
        return edad
