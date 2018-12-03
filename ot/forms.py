from django import forms
from .models import Cliente_Tecnico


estado = (
	('1','Pendiente'),
	('2','Terminada'),
)


class Cliente_TecnicoForm(forms.ModelForm):
	class Meta:
		model = Cliente_Tecnico
		fields = [
			'id_cliente',
			'id_tecnico',
			'fecha',
		]
		labels = {
			'id_cliente' : 'Cliente',
			'id_tecnico' : 'Técnico',
			'fecha' : 'Fecha de visita',
		}
		widgets = {
			'id_cliente' : forms.Select(attrs={'class' : 'form-control'}),
			'id_tecnico' : forms.Select(attrs={'class' : 'form-control'}),
			'fecha' : forms.TextInput(attrs={'class' : 'form-control'}),
		}


class Cliente_TecnicoFormFull(forms.ModelForm):
	class Meta:
		model = Cliente_Tecnico
		fields = [
			'id_cliente',
			'id_tecnico',
			'fecha',
			'hora_inicio',
			'hora_termino',
			'id_ascensor',
			'fallas',
			'piezas',
			'encargado',
			'estado',
		]
		labels = {
			'id_cliente' : 'Cliente',
			'id_tecnico' : 'Técnico',
			'fecha' : 'Fecha de visita',
			'hora_inicio' : 'Hora de Inicio',
			'hora_termino' : 'Hora de Término',
			'id_ascensor' : 'Ascensor trabajado',
			'fallas' : 'Fallas encontradas',
			'piezas' : 'Piezas Cambiadas',
			'encargado' : 'Nombre persona a cargo',
			'estado' : 'Estado',
		}
		widgets = {
			'id_cliente' : forms.Select(attrs={'class' : 'form-control'}),
			'id_tecnico' : forms.Select(attrs={'class' : 'form-control'}),
			'fecha' : forms.TextInput(attrs={'class' : 'form-control'}),
			'hora_inicio' : forms.TextInput(attrs={'class' : 'form-control'}),
			'hora_termino' : forms.TextInput(attrs={'class' : 'form-control'}),
			'id_ascensor' : forms.TextInput(attrs={'class' : 'form-control'}),
			'fallas' : forms.Textarea(attrs={'class' : 'form-control', 'rows':'3'}),
			'piezas' : forms.Textarea(attrs={'class' : 'form-control', 'rows':'3'}),
			'encargado' : forms.TextInput(attrs={'class' : 'form-control'}),
			'estado' : forms.Select(choices = estado,attrs={'class' : 'form-control'}),
		}

