from django.db import models
from categorys.models import * 
from user.models import * 

# Create your models here.
class Product(models.Model):
	condition_types = [
		(1,"New"),
		(2,"Used"),
		(3,"Unpacked")
	]
	status_types = [
      (1,'ACTIVE'),
      (2,'INACTIVE'),
      (3,'SOLD')

	]
	title = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	description = models.TextField()
	
	category = models.ForeignKey(Categorys,on_delete=models.SET_NULL,blank=True,null=True)
	location = models.ForeignKey(Region,on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
	User = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
	discount = models.IntegerField()
	slug =  models.SlugField(unique=True)
	condition = models.SmallIntegerField(choices=condition_types, default=1)
	status = models.SmallIntegerField(choices=status_types, default=1)
	createdat = models.DateField(auto_now_add=True)
	update_at = models.DateField(auto_now=True)
	def __str__(self):
		return self.title
	def save(self,*args,**kwargs):
		if self.discount:
			self.price -= (self.price * self.discount / 100)
		super().save(*args,**kwargs)

class ProductView(models.Model):
	product = models.OneToOneField(Product,on_delete=models.CASCADE)
	view_count = models.IntegerField(default=0)
class ProductImage(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
	image = models.ImageField(upload_to='products/',)
	is_main = models.BooleanField(default=False)	
