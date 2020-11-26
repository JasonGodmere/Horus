
from django.db import models

# Custom user authentication model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass

# Profile is just an extension of the user (one to one)
class Profile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
	)

	def __str__(self):
		return self.user.username




# Cluster model
class Cluster(models.Model):
	name = models.CharField(max_length=100, unique=True)
	created_on = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(auto_now=True)

	owner = models.ForeignKey('User', on_delete=models.CASCADE)
	contributors = models.ManyToManyField('Profile', blank=True, null=True)


	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']