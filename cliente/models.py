from django.db import models


# Create your models here.
class Cliente(models.Model):
	nombre 		= models.CharField(max_length = 100)
	direccion 	= models.CharField(max_length = 100)
	region		= models.CharField(max_length = 100)
	comuna		= models.CharField(max_length = 100)
	telefono	= models.CharField(max_length = 100)
	email		= models.EmailField(max_length = 100)

	def __str__(self):
		return self.nombre


class Ascensor(models.Model):
	numero		= models.CharField(max_length = 100)
	modelo 		= models.CharField(max_length = 100)
	id_cliente	= models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.numero
