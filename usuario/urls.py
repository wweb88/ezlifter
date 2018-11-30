from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import tecnico_list, tecnico_new, tecnico_edit


urlpatterns = [
    url(r'^listar$', login_required(tecnico_list.as_view()), name='tecnico_listar'),
    url(r'^nuevo$', login_required(tecnico_new.as_view()), name='tecnico_crear'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(tecnico_edit.as_view()), name='tecnico_editar'),
]