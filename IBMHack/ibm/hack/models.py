from django.db import models
from time import time
import datetime
from datetime import date
from datetime import datetime    


class person(models.Model):
	unique_id = models.IntegerField(null=False,primary_key=True)
	name = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	weight = models.FloatField(null=False, default=0)
	height = models.FloatField(null=False, default=0)
	age = models.IntegerField(null=False, default=0)
	gender = models.CharField(max_length=10)
	activity = models.IntegerField(null=False)
	tee = models.FloatField(default=0)
	
	
	def __str__(self):
		return str(self.unique_id) + ' / ' + self.name


class images(models.Model):
	image_name = models.CharField(max_length=40)
	date = models.DateField(("Date"), auto_now_add=True)
	name = models.CharField(max_length=30, null=False, default='')
	item_name = models.CharField(max_length=40, default='')
	calorie = models.IntegerField(default=0)

	def __str__(self):
		return self.name



