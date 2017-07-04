# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
class Contacto(models.Model):
	nombre = models.CharField(max_length=70)
	apellido = models.CharField(max_length=70)
	email = models.EmailField(max_length=100)
	telefono = models.CharField(max_length=9)
	direccion = models.TextField(null=True, blank=True,)
	imagen = models.ImageField(null=True, blank=True, upload_to = "static/img")
	#AIzaSyBR0wHaBAr7d-RaSe361SgMxJ-7GvGEkO8

	def __str__(self):
		return self.nombre