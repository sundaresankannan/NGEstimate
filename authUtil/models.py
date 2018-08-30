from django.db import models
from django.utils import timezone

# Create your models here.
class user_mstr(models.Model):
	
	login_id= models.CharField(max_length=20)
	login_pwd = models.CharField(max_length=120)
	last_name= models.CharField(max_length=18)
	first_name= models.CharField(max_length=13)
	startdate = models.DateTimeField()
	enddate= models.DateTimeField()
	
	def __str__(self):
		return self.last_name +" "+ self.first_name

class estimate_mstr(models.Model):
	estimate_id = models.CharField(max_length=20)