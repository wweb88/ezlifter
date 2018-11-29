from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import CustomUser

from .forms import CustomUserCreationForm

# Create your views here.

class RegistroUsuario(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('home')
	template_name = 'usuario/registrar.html'


class tecnico_list(ListView):
	model = CustomUser
	queryset = CustomUser.objects.filter(grupo='1')
	template_name = 'usuario/tecnico_list.html'
	context_object_name = 'tecnicos'