from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomUser(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30,null=False,blank=True)
	phone_number = models.CharField(max_length=13,null=False,blank=False)
	image = models.ImageField(upload_to='profile/',null=True,blank=True)
	def __str__(self):
		return self.first_name