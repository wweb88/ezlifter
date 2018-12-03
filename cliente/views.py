from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Cliente, Ascensor
from .forms import ClienteForm, ClienteEditForm, AscensorForm



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



def ascensor_list(request, id_cliente):
	cliente = Cliente.objects.get(id = id_cliente)
	ascensores = Ascensor.objects.filter(id_cliente = cliente).order_by('-id')

	return render(request, 'cliente/cliente_ascensor_list.html', {'cliente': cliente, 'ascensores': ascensores})

# class ascensor_list(ListView):
#	model = Ascensor
#	template_name = 'cliente/cliente_ascensor_list.html'
#	context_object_name = 'ascensores'
#
#	def get_queryset(self, **kwargs):
#		cliente = self.kwargs['pk']
#		return Ascensor.objects.filter(pertenece = cliente).order_by('-id')


def ascensor_new(request, id_cliente):
	cliente = Cliente.objects.get(id = id_cliente)

	if request.method == 'POST':
		form = AscensorForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('cliente_listar')
	else:
		form = AscensorForm()

	return render(request, 'cliente/ascensor_form.html', {'form' : form , 'cliente' : cliente })