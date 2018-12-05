from __future__ import unicode_literals

from django.db import models

from django.core.mail import send_mail

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


grupo = (
	('1','Técnico'),
	('2','Administrador'),
)

class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
	email		= models.CharField(max_length = 255, unique=True)
	first_name 	= models.CharField(max_length=30, blank=True)
	last_name 	= models.CharField(max_length=30, blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	is_active 	= models.BooleanField(default=True)
	is_staff	= models.BooleanField(default=False)
	nombre 		= models.CharField(max_length = 255, blank=True, null=True)
	grupo		= models.CharField(max_length = 50, choices = grupo, default='1')

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return '{} {}'.format(self.first_name, self.last_name)

	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.email], **kwargs)
	
	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)



