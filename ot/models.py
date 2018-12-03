from django.db import models
from usuario.models import CustomUser
from cliente.models import Cliente, Ascensor
# Create your models here.

estado = (
	('1','Pendiente'),
	('2','Terminada'),
)

class Cliente_Tecnico(models.Model):
	id_cliente	= models.ForeignKey(Cliente, on_delete=models.CASCADE)
	id_tecnico	= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	fecha 		= models.DateTimeField()
	hora_inicio	= models.DateTimeField(null=True, blank=True)
	hora_termino = models.DateTimeField(null=True, blank=True)
	id_ascensor	= models.ForeignKey(Ascensor, null=True, blank=True, on_delete=models.CASCADE)
	fallas		= models.CharField(max_length=255, null=True, blank=True)
	piezas		= models.CharField(max_length=255, null=True, blank=True)
	encargado	= models.CharField(max_length=100, null=True, blank=True)
	estado		= models.CharField(max_length = 50, choices = estado, default='1')

	def __str__(self):
		return self.id