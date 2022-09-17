from django import forms
from models import Empresa, Documento





class DocumentoForm(forms.Form):
    documento = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
