from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

import platform

# Create your views here.

def index(request):
	return render(request, 'hub/index.html', {
		'server_id': mark_safe(json.dumps(platform.node()))
	})
