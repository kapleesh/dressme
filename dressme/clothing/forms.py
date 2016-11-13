from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	def __init__(self, *args, **kwargs):
		super(forms.ModelForm, self).__init__(*args, **kwargs)
		self.fields['username'].help_text = None

	class Meta:
		model = StormChaser
		fields = ('first_name', 'last_name', 'username', 'email', 'password', 'zipcode')

#Unfished EventForm class
#Useful in eventAdd, eventAuth
#Top/bottom/extra outfit can't be represented in google
#instead, condensed into 1 string.
#database can keep it as 3 separate forms.

# class EventForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(forms.ModelForm, self).__init__(*args, **kwargs)

#     class Meta:
#         model = Events
#         fields = ('description', 'top-outfit', 'bottom-outfit', 'extra-outfit', 'cityState', 'day')
