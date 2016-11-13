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

class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Events
        fields = ('description', 'top-outfit', 'bottom-outfit', 'extra-outfit', 'cityState', 'day')
