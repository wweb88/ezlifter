from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import ot_list, ot_new, ot_edit, ot_start, ot_view


urlpatterns = [
    url(r'^listar$', login_required(ot_list.as_view()), name='ot_listar'),
    url(r'^nuevo$', login_required(ot_new.as_view()), name='ot_crear'),
    url(r'^editar/(?P<id_ot>\d+)/$', login_required(ot_edit), name='ot_editar'),
    url(r'^iniciar-ot/(?P<id_ot>\d+)/$', login_required(ot_start), name='ot_iniciar'),
    url(r'^ver-ot/(?P<id_ot>\d+)/$', login_required(ot_view), name='ot_ver'),
    
]