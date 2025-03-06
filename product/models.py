from django.db import models
from categorys.models import * 
# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to='products',null=True,blank=True)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	description = models.TextField()
	createdat = models.DateField(auto_now_add=True)
	update_at = models.DateField(auto_now=True)
	category = models.ForeignKey(Categorys,on_delete=models.SET_NULL,blank=True,null=True)
	discount = models.IntegerField()
	slug =  models.SlugField(unique=True)
	def __str__(self):
		return self.name
	def save(self,*args,**kwargs):
		if self.discount:
			self.price -= (self.price * self.discount / 100)
		super().save(*args,**kwargs)