from django.db import models
from product.models import country
# Create your models here.
class Categorys(models.Model):
	name = models.CharField(max_length=35)
	image = models.ImageField(upload_to='categorys/',blank=True,null=True)
	is_option = models.BooleanField(default=False)
	for_footer = models.BooleanField(default=False)
	for_mid_part = models.BooleanField(default=False)
	for_header = models.BooleanField(default=False)
	slug = models.SlugField(unique=True)
	parent = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
	def __str__(self):
		return self.name



class Region(models.Model):
	country_id = models.ForeignKey(country,on_delete=models.CASCADE,default=1)
	name = models.CharField(max_length=50,null=False,blank=True)
	sorting = models.SmallIntegerField(null=False,blank=False,unique=True)

	def __str__(self):
		return self.name
class Brand(models.Model):
	name = models.CharField(max_length=30,null=False,blank=False)
	def __str__(self):
		return self.name