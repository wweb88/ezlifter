from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Cliente, Ascensor
from .forms import ClienteForm, ClienteEditForm


# Create your views here.
class cliente_list(ListView):
	model = Cliente
	queryset = Cliente.objects.order_by('-id')
	template_name = 'cliente/cliente_list.html'
	context_object_name = 'clientes'

class cliente_new(CreateView):
	model =	Cliente
	form_class = ClienteForm
	template_name = 'cliente/cliente_form.html'
	success_url = reverse_lazy('cliente_listar')

class cliente_edit(UpdateView):
	model =	Cliente
	form_class = ClienteEditForm
	template_name = 'cliente/cliente_edit.html'
	success_url = reverse_lazy('cliente_listar')


class ascensor_list(ListView):
	model = Ascensor
	queryset = Cliente.objects.order_by('-id')
	template_name = 'cliente/cliente_list.html'
	context_object_name = 'clientes'