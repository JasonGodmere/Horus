from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

import json
import platform

# Create your views here.

@login_required #login url in settings.py set under LOGIN_URL
def index(request):
	return render(request, 'hub/index.html', {
		'server_id': mark_safe(json.dumps(platform.node()))
	})