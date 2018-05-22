# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings        #clase 21
from django.core.mail import send_mail  #clase 21
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado
# Create your views here.
def inicio(request):
    titulo = "hOlA"
    abc = "321"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s" %(request.user)    #clase 18
    form= RegModelForm(request.POST or None)
    #print(dir(form))
    context = {
        "titulo": titulo,
        "abc" : abc,
        "el_form": form,
        }

    if form.is_valid():
        instance = form.save(commit=False)  #clase 19
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")

        if not instance.nombre:
            instance.nombre= "Persona"
        instance.save()
        context = {
            "titulo": "Gracias %s!" %(nombre),
            }
        if not nombre:
            context= {
                "titulo":"Gracias persona sin nombre"
            }
        print instance
        print instance.timestamp
        # form_data = form.cleaned_data
        # abc = form_data.get("email")
        # abc2 = form_data.get("nombre")
        # obj = Registrado.objects.create(email=abc, nombre=abc2)

        #hecho de otra forma, es lo mismo que:
        #obj= Registrado()
        #obj.email= abc
        #obj.save()
    if request.user.is_authenticated() and request.user.is_staff:
        #clase 39
        queryset = Registrado.objects.all().order_by("-timestamp").filter(nombre__icontains="per") 
        # i = 1
        # for instance in Registrado.objects.all():
        #     print(i)
        #     print(instance.nombre)
        #     i +=1
        context = {
            "queryset":queryset
        }
    return render(request, "inicio.html",context)

def contact(request):
    titulo = "Contacto"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():   #clase 20
        #     print(key, value)

        # for key in form.cleaned_data:
        #     print (key)
        #     print (form.cleaned_data.get(key))


        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Form prueba contacto django'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otroemail@gmail.com"]
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            [email_to],
            fail_silently=False
            )
        # print (email, mensaje, nombre)
    context = {
        "form": form,
        "titulo":titulo,
    }
    return render(request, "forms.html", context)
