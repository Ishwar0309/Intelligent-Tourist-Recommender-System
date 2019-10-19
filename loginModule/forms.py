from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	contact = forms.IntegerField(required = True)
	class Meta:
		model = User 
		fields = ['username' , 'email' ,'first_name','last_name' ,'contact' ,'password1' , 'password2']
