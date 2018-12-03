from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import cliente_list, cliente_new, cliente_edit, ascensor_list, ascensor_new


urlpatterns = [
    url(r'^listar$', login_required(cliente_list.as_view()), name='cliente_listar'),
    url(r'^nuevo$', login_required(cliente_new.as_view()), name='cliente_crear'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(cliente_edit.as_view()), name='cliente_editar'),
	#url(r'^ascensor-lista/(?P<pk>\d+)/$', login_required(ascensor_list.as_view()), name='ascensor_listar'),
	url(r'^ascensor-lista/(?P<id_cliente>\d+)/$', login_required(ascensor_list), name='ascensor_listar'),
	url(r'^nuevo-ascensor/(?P<id_cliente>\d+)/$', login_required(ascensor_new), name='ascensor_crear'),
]