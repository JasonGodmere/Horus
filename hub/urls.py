
from django.urls import path

from . import views

app_name = 'hub'

urlpatterns = [
	path('', views.login_request, name='login'),
	path('logout/', views.logout_request, name='logout'),
	path('hub/', views.hub, name='hub'),
	#path('<str:room_name>/', views.room, name='room'),
]