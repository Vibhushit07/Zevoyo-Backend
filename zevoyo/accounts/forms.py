from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'firstName', 'lastName', 'email', 'password1', 'password2']

class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['phoneNumber', 'salary']

class editEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = ['phoneNumber', 'salary']

class editUser(ModelForm):
    class Meta:
        model = Employee
        fields = ['firstName', 'lastName', 'email']

class editGuest(ModelForm):
    class Meta:
        model = Guest
        fields = ['phoneNumber']

class ROLES(forms.Form):
    ROLES_TYPES = [
        ('manager', 'manager'),
        ('receptionist', 'receptionist'),
        ('staff', 'staff'),
    ]
    ROLES_TYPES = forms.CharField(
        widget = forms.RadioSelect(choices = ROLES_TYPES))