from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import CustomUser

from .forms import CustomUserCreationForm

# Create your views here.

class tecnico_list(ListView):
	model = CustomUser
	queryset = CustomUser.objects.filter(grupo='1').order_by('-id')
	template_name = 'usuario/tecnico_list.html'
	context_object_name = 'tecnicos'

class tecnico_new(CreateView):
	model =	CustomUser
	form_class = CustomUserCreationForm
	template_name = 'usuario/tecnico_form.html'
	success_url = reverse_lazy('tecnico_listar')

class tecnico_edit(UpdateView):
	model =	CustomUser
	form_class = CustomUserCreationForm
	template_name = 'usuario/tecnico_edit.html'
	success_url = reverse_lazy('tecnico_listar')