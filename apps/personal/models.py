from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Perfil(models.Model):
	"""Agregando peesonal"""
	user = models.ForeignKey(User)
	direccion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=100)

