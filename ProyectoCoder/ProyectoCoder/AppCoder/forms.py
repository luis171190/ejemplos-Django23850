from django import forms

class EstadioFormulario(forms.Form):
    
    #campos
    direccion = forms.CharField()
    anioFund = forms.IntegerField()