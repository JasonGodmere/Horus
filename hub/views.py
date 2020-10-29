from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

import json
import platform

# Create your views here.

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				#messages.info(request, f"You are now logged in as {username}")
				return redirect('/hub')
			else:
				pass
				#messages.error(request, "Invalid username or password.")
		else:
			pass
			#messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request = request,
				  template_name = "hub/login.html",
				  context={"form":form})

def logout_request(request):
	logout(request)
	return redirect('/')

@login_required #login url in settings.py set under LOGIN_URL
def hub(request):
	return render(request, 'hub/hub.html', {
		'server_id': mark_safe(json.dumps(platform.node()))
	})