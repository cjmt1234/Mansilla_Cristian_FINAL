#import requests
from django import forms
from EvaFinalApp import models

class FormInscritos(forms.ModelForm):

    
    class Meta:
        model = models.Inscritos
        fields =  ['nombre', 'telefono', 'fechaInscripcion','institucion', 'hora', 'estado', 'observacion']

        ESTADOS = [('reservado', 'RESERVADO'),('completada','COMPLETADA'), ('anulada','ANULADA'), ('no asisten','NO ASISTEN')]

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre','class':'form-control'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese el número teléfono ej:(9xxxxxxxx)', 'class':'form-control'}),
            'fechaInscripcion': forms.TextInput(attrs={'placeholder': 'Ingrese la fecha de reserva', 'class':'form-control', 'type':'date'}),
            'institucion': forms.Select(attrs={'class':'form-select'}),
            'hora': forms.TextInput(attrs={'placeholder': 'Ingrese la hora de reserva', 'class':'form-control', 'type':'time'}),
            'estado': forms.Select(choices=ESTADOS, attrs={'class':'form-select'}),
            'observacion': forms.Textarea(attrs={'placeholder': 'Ingrese las observaciones', 'class':'form-control'}),
        }



    
    def clean_nombre(self):
            nombre = self.cleaned_data['nombre']

            if len(nombre) > 80:
                raise forms.ValidationError('El nombre no debe tener más de 80 caracteres.')

            return nombre
    
    def clean_telefono(self):
            telefono= self.cleaned_data['telefono']

            if len(telefono) != 9 or int(telefono) >= 1000000000 or int(telefono) < 900000000:
                raise forms.ValidationError('El telefono no es válido.')

            return telefono


class FormInstitucion(forms.ModelForm):

    
    class Meta:
        model = models.Institucion
        fields =  ['nombre']

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre','class':'form-control'}),
           
        }