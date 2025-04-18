from django.db import models
from categorys.models import * 
from django.utils.text import slugify
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
	category = models.ForeignKey('categorys.Categorys',on_delete=models.SET_NULL,blank=True,null=True)
	location = models.ForeignKey('categorys.Region',on_delete=models.CASCADE)
	brand = models.ForeignKey('categorys.Brand',on_delete=models.CASCADE)
	User = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
	discount = models.IntegerField()
	slug =  models.SlugField()
	condition = models.SmallIntegerField(choices=condition_types, default=1)
	status = models.SmallIntegerField(choices=status_types, default=1)
	createdat = models.DateField(auto_now_add=True)
	update_at = models.DateField(auto_now=True)
	def __str__(self):
		return self.title
	def save(self,*args,**kwargs):
		if self.discount:
			self.price -= (self.price * self.discount / 100)
			self.slug = slugify(self.title)
		super().save(*args,**kwargs)

class ProductView(models.Model):
	product = models.OneToOneField(Product,on_delete=models.CASCADE)
	view_count = models.IntegerField(default=0)
class ProductImage(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
	image = models.ImageField(upload_to='products/',)
	is_main = models.BooleanField(default=False)
class country(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name
class Area(models.Model):
	name = models.CharField(max_length=255)
	state = models.ForeignKey('categorys.Region',on_delete=models.CASCADE)
	def __str__(self):
		return self.name
class ContactDetail(models.Model):
	product = models.OneToOneField(Product,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	phone_n = models.CharField(max_length=300)
	enter_address = models.TextField()
	country = models.ForeignKey('product.country',on_delete=models.CASCADE)
	state = models.ForeignKey('categorys.Region',on_delete=models.CASCADE)
	city_area = models.ForeignKey('product.Area',on_delete=models.CASCADE,default="Toshkent")

	def __str__(self):
		return self.product