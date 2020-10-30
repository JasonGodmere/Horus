from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
				return redirect('hub:index')
			else:
				pass
				#messages.error(request, "Invalid username or password.")
		else:
			pass
			#messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request = request,
				  template_name = "main/login.html",
				  context={"form":form})

def logout_request(request):
	logout(request)
	return redirect('/')