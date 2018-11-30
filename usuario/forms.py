from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


grupo = (
	('1','Técnico'),
	('2','Administrador'),
)
estado = (
	('True','Activo'),
	('False','Inactivo'),
)

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = [
			'email',
			'nombre',
			'first_name',
			'last_name',
			'grupo',
			'is_active',
		]
		labels = {
			'email' : 'Email',
			'nombre' : 'Nombre',
			'first_name' : 'Nombre',
			'last_name' : 'Apellido',
			'grupo' : 'Grupo',
			'is_active' : 'Estado',
		}
		widgets = {
			'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
			'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
			'grupo' : forms.Select(choices = grupo,attrs={'class' : 'form-control'}),
			'is_active' : forms.Select(choices = estado,attrs={'class' : 'form-control'}),
		}
