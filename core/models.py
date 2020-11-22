
from django.db import models

# Custom user model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass




# Cluster model
class Cluster(models.Model):
	name = models.CharField(max_length=100, unique=True)
	created_on = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']