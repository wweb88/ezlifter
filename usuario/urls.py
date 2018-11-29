from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import tecnico_list


urlpatterns = [
    url(r'^listar$', login_required(tecnico_list.as_view()), name='tecnico_listar'),
]