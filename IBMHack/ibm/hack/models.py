from django.db import models
from time import time
from datetime import date


class person(models.Model):
	unique_id = models.IntegerField(null=False,primary_key=True)
	name = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	weight = models.FloatField(null=False, default=0)
	height = models.FloatField(null=False, default=0)
	age = models.IntegerField(null=False, default=0)
	gender = models.CharField(max_length=10)
	activity = models.IntegerField(max_length=20)
	tee = models.FloatField(default=0)
	
	
	def __str__(self):
		return str(self.unique_id) + ' / ' + self.name



