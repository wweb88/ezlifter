"""ezlifterWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'^home$', login_required(views.home), name="home"),
    url(r'^tecnicos/', include('usuario.urls')),
    url(r'^clientes/', include('cliente.urls')),
    url(r'^ot/', include('ot.urls')),

    url(r'^$', login, {'template_name':'usuario/login.html'}, name="login"),
    url(r'^logout/', logout_then_login, name="logout"),
    url(r'^reset/password_reset$', password_reset, {'template_name' : 'registration/password_reset_form.html', 'email_template_name' : 'registration/password_reset_email.html'}, name='password_reset'),
    url(r'^reset/password_reset_done$', password_reset_done, {'template_name' : 'registration/password_reset_done.html'}, name="password_reset_done" ),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name' : 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^reset/done', password_reset_complete, {'template_name' : 'registration/password_reset_complete.html'}, name="password_reset_complete" ),

    url('accounts/', include('allauth.urls')),
    #url('', include('social_django.urls', namespace='social')),
]


