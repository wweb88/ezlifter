from django.shortcuts import render, redirect

from allauth.socialaccount.signals import pre_social_login
from allauth.account.utils import perform_login
from allauth.utils import get_user_model
from allauth.exceptions import ImmediateHttpResponse

from django.dispatch import receiver

from usuario.models import CustomUser


# Create your views here.
def home(request):
	return render(request, 'home/index.html',{ })



@receiver(pre_social_login)
def link_to_local_user(sender, request, sociallogin, **kwargs):
	''' Login and redirect
	This is done in order to tackle the situation where user's email retrieved
	from one provider is different from already existing email in the database
	(e.g facebook and google both use same email-id). Specifically, this is done to
	tackle following issues:
	* https://github.com/pennersr/django-allauth/issues/215

	'''
	email_address = sociallogin.account.extra_data['email']
	users = CustomUser.objects.filter(email = email_address)
	if users:
		# allauth.account.app_settings.EmailVerificationMethod
		perform_login(request, users[0], email_verification = 'optional')
		raise ImmediateHttpResponse(redirect('home'))
	else:
		raise ImmediateHttpResponse(redirect('login'))