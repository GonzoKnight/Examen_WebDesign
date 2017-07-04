# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def contact_list(request):
    template_name = 'contact_list.html'
    return render (request, template_name, {})

def inicio(request):
	template_name = 'contacto/default.html'
	return render (request, template_name, {})

def lista(request):
	template_name = 'contacto/lista.html'
	return render (request, template_name, {})

def informacion(request):
	template_name = 'contacto/informacion.html'
	return render (request, template_name, {})

#vista opcional
def noticia(request):
	template_name = 'contacto/noticia_detalle.html'
	return render (request, template_name, {})
