from django import forms
from .models import Cliente, Ascensor

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = [
			'nombre',
			'telefono',
			'email',
			'direccion',
			'region',
			'comuna',
		]
		labels = {
			'nombre' : 'Nombre',
			'telefono' : 'Teléfono',
			'email' : 'Email',
			'direccion' : 'Dirección',
			'region' : 'Región',
			'comuna' : 'Comuna',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'telefono' : forms.TextInput(attrs={'class' : 'form-control solo-numero'}),
			'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
			'direccion' : forms.TextInput(attrs={'class' : 'form-control'}),
			'region' : forms.HiddenInput(attrs={'class' : 'form-control'}),
			'comuna' : forms.HiddenInput(attrs={'class' : 'form-control'}),
		}

class ClienteEditForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = [
			'nombre',
			'telefono',
			'email',
			'direccion',
			'region',
			'comuna',
		]
		labels = {
			'nombre' : 'Nombre',
			'telefono' : 'Teléfono',
			'email' : 'Email',
			'direccion' : 'Dirección',
			'region' : 'Región',
			'comuna' : 'Comuna',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'telefono' : forms.TextInput(attrs={'class' : 'form-control solo-numero'}),
			'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
			'direccion' : forms.TextInput(attrs={'class' : 'form-control'}),
			'region' : forms.TextInput(attrs={'class' : 'form-control'}),
			'comuna' : forms.TextInput(attrs={'class' : 'form-control'}),
		}

class AscensorForm(forms.ModelForm):
	class Meta:
		model = Ascensor
		fields = [
			'numero',
			'modelo',
			'id_cliente',
		]
		labels = {
			'numero' : 'Número',
			'modelo' : 'Modelo',
		}
		widgets = {
			'numero' : forms.TextInput(attrs={'class' : 'form-control'}),
			'modelo' : forms.TextInput(attrs={'class' : 'form-control solo-numero'}),
			'id_cliente' : forms.HiddenInput(),
		}

class AscensorFormEdit(forms.ModelForm):
	class Meta:
		model = Ascensor
		fields = [
			'numero',
			'modelo',
		]
		labels = {
			'numero' : 'Número',
			'modelo' : 'Modelo',
		}
		widgets = {
			'numero' : forms.TextInput(attrs={'class' : 'form-control'}),
			'modelo' : forms.TextInput(attrs={'class' : 'form-control solo-numero'}),
		}
