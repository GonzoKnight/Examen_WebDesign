from django.conf.urls import url
from contacto import views

app_name = 'contacto'

urlpatterns = [
    #url(r'^list/$', views.contact_list, name='contact_list'),

	url(r'^list/$', views.contact_list, name='lista de contactos'),
	url(r'^inicio/$', views.inicio, name='contacto_inicio'),
    
    #url(r'^new/$', views.movie_form, name='movie_create'),
    #url(r'^edit/(?P<pk>\d+)$', views.movie_update, name='movie_edit'),
    #url(r'^delete/(?P<pk>\d+)$', views.movie_delete, name='movie_delete'),

]
