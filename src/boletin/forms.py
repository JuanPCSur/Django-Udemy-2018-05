from django import forms

#Clase 16 Model form
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre","email"]

    #validaciones personalizadas clase 17
    def clean_email(self):
        email =  self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not extension == "edu":
            raise forms.ValidationError("Usa un correo .edu")
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        #validaciones personalizadas clase 17
        return nombre

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

    # def clean_email(self):
    #     email =  self.cleaned_data.get("email")
    #     email_base, proveedor = email.split("@")
    #     dominio, extension = proveedor.split(".")
    #     if not extension == "edu":
    #         raise forms.ValidationError("Usa un correo .edu")
    #     return email
