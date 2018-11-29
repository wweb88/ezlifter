from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


grupo = (
	('1','Técnico'),
	('2','Administrador'),
)

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = [
			'email',
			'nombre',
		]
		labels = {
			'email' : 'Email',
			'nombre' : 'Nombre',
		}
		widgets = {
			'email' : forms.TextInput(attrs={'class' : 'form-control'}),
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
		}



class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('email',)