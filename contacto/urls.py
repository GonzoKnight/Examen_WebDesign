from django.conf.urls import url
from contacto import views

app_name = 'contacto'

urlpatterns = [
    url(r'^inicio/$', views.inicio, name='contacto_inicio'),
    url(r'^noticia/$', views.noticia, name='contacto_noticia'),
    url(r'^lista/$', views.lista, name='contacto_lista'),
	url(r'^informacion/$', views.informacion, name='contacto_informacion'),
        

    #url(r'^new/$', views.movie_form, name='movie_create'),
    #url(r'^edit/(?P<pk>\d+)$', views.movie_update, name='movie_edit'),
    #url(r'^delete/(?P<pk>\d+)$', views.movie_delete, name='movie_delete'),

]
