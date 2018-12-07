from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Cliente_Tecnico
from cliente.models import Ascensor, Cliente

from .forms import Cliente_TecnicoForm, Cliente_TecnicoFormFull, Cliente_TecnicoFormStart

#from .forms import ClienteForm
class ot_list(ListView):
	model = Cliente_Tecnico
	queryset = Cliente_Tecnico.objects.order_by('fecha')
	template_name = 'ot/ot_list.html'
	context_object_name = 'ots'

class ot_new(CreateView):
	model =	Cliente_Tecnico
	form_class = Cliente_TecnicoForm
	template_name = 'ot/ot_form.html'
	success_url = reverse_lazy('ot_listar')

def ot_edit(request, id_ot):
	ot = Cliente_Tecnico.objects.get(id = id_ot)
	ascensores = Ascensor.objects.filter(id_cliente = ot.id_cliente).order_by('-id')
	if request.method == 'GET':
		form = Cliente_TecnicoFormFull(instance = ot)
	else:
		form = Cliente_TecnicoFormFull(request.POST, instance = ot)
		if form.is_valid():
			form.save()
		return redirect('ot_listar')
	return render(request, 'ot/ot_edit.html', {'form' : form , 'ascensores' : ascensores })


def ot_start(request, id_ot):
	ot = Cliente_Tecnico.objects.get(id = id_ot)
	ascensores = Ascensor.objects.filter(id_cliente = ot.id_cliente).order_by('-id')
	if request.method == 'GET':
		form = Cliente_TecnicoFormStart(instance = ot)
	else:
		form = Cliente_TecnicoFormStart(request.POST, instance = ot)
		if form.is_valid():
			form.save()
		return redirect('ot_listar')
	return render(request, 'ot/ot_start.html', {'form' : form , 'ascensores' : ascensores, 'ot' : ot })


def ot_view(request, id_ot):
	ot = Cliente_Tecnico.objects.get(id = id_ot)
	return render(request, 'ot/ot_view.html', {'ot' : ot })


