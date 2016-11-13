from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings

from .forms import *
from .models import *
from .backends import *

from oauth2client import client, file, tools

from apiclient.discovery import build


import httplib2
import json

# Create your views here.

flow = client.flow_from_clientsecrets(
	    'clothing/client_secrets.json',
	    scope='https://www.googleapis.com/auth/calendar',
	    redirect_uri='http://localhost:8000/calendarHelper')

CAL = None

@login_required(login_url="/user_login/")
def index(request):
	return render(request, "clothing/index.html")

def logout_view(request):
	logout(request)
	logged_out = True
	return render(request, "clothing/login.html", {'logged_out': logged_out})

def testing(request):
	auth_uri = flow.step1_get_authorize_url()
	return redirect(auth_uri)

def calendarHelper(request):
	credentials = flow.step2_exchange(request.GET.get('code', ''))
	http_auth = credentials.authorize(httplib2.Http())
	CAL = build('calendar', 'v3', http=http_auth)
	primary = CAL.calendars()
	cal = primary.get(calendarId='primary').execute()
	calID = cal['id']
	calTime = cal['timeZone']
	request.session['calendarInfo'] = {'calID': calID, 'calTime': calTime}
	return redirect('calendar')

def calendar(request):
	calID = request.session['calendarInfo']['calID']
	calTime = request.session['calendarInfo']['calTime']
	return render(request, "clothing/calendar.html", {'calID':calID, 'calTime':calTime})

def eventAdd(request):
	event = {
		'description': '',
		'start': {
			'date': ''
		},
		'end': {
			'date': ''
		},
		'summary': 'include all 3 outfits',
	}
	

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
