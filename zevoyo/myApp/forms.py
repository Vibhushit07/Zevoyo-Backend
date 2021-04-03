from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	# email = forms.EmailField(required=True)
	# phone_no = forms.CharField(max_length = 20)
	# first_name = forms.CharField(max_length = 20)
	# last_name = forms.CharField(max_length = 20)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	# def save(self, commit=True):
	# 	user = super(UserRegisterForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	# 	return user

