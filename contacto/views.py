# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from contacto.models import Contacto
from django.shortcuts import render

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

#vista opcional
def noticia(request):
	template_name = 'contacto/noticia_detalle.html'
	return render (request, template_name, {})
