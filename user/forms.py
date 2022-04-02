from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',

		]
		labels = {
			'username': 'Username:',
			'first_name': 'First Name:',
			'last_name': 'Last name:',

		}