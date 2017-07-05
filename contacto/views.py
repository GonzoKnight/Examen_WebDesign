# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from contacto.models import Contacto
from contacto.forms import ContactoForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


# Create your views here.

def inicio(request):
	template_name = 'contacto/default.html'
	return render (request, template_name, {})

def lista(request):
	contacto = Contacto.objects.all().order_by('id')
	contexto = {'contactos':contacto}
	template_name = 'contacto/lista.html'
	return render (request, template_name, contexto)

def informacion(request):
	template_name = 'contacto/informacion.html'
	return render (request, template_name, {})

def contacto_update(request, pk) :
    template_name = 'contacto/informacion.html'
    # movie = Movie.objects.get(pk=pk)
    contacto = get_object_or_404(Contacto, pk=pk)
    # select * from movie WHERE id = xx

    form = ContactoForm(request.POST or None, instance=contacto)

    if form.is_valid() :
        form.save()
        return HttpResponseRedirect('contacto_informacion')

    return render(request, template_name, {'form': form})

#vista opcional
def noticia(request):
	template_name = 'contacto/noticia_detalle.html'
	return render (request, template_name, {})
