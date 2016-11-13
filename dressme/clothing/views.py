from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings

from .forms import *
from .models import *
from .backends import *

from oauth2client import client

import json

# Create your views here.

@login_required(login_url="/user_login/")
def index(request):
	return render(request, "clothing/index.html")

def logout_view(request):
	logout(request)
	logged_out = True
	return render(request, "clothing/login.html", {'logged_out': logged_out})

def testing(request):
	flow = client.flow_from_clientsecrets(
	    'clothing/client_secrets.json',
	    scope='https://www.googleapis.com/auth/drive.metadata.readonly',
	    redirect_uri='http://localhost:8000/calendar')
	auth_uri = flow.step1_get_authorize_url()
	return redirect(auth_uri)

def calendar(request):
	return render(request, "clothing/login.html", {})

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(str(user_form.errors))
	else:
		user_form = UserForm()
	return render(request, "clothing/register.html", {'user_form': user_form, 'registered': registered})

def user_login(request):
	context = RequestContext(request)

	wrong_login = False
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = CustomBackend().authenticate(username, password)
		if user is not None:
			login(request, user)
			logged_in = True
			return render(request, "clothing/index.html", {'logged_in': logged_in})
		else:
			wrong_login = True
			return render(request, "clothing/login.html", {'wrong_login': wrong_login})
	elif request.user.is_authenticated(): 
		return render(request, "clothing/index.html")
	else:
		return render(request, "clothing/login.html", {'wrong_login': wrong_login})
