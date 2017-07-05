# -*- coding: utf-8 -*-
from django.forms import ModelForm
from contacto.models import Contacto
class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','apellido','email','telefono','direccion','imagen']
