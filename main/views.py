from django.shortcuts import render,get_object_or_404
from categorys.models import *
from product.models import *
from user.models import *
# Create your views here.
def main(request):
	for_header = Categorys.objects.filter(for_header=True)
	for_footer = Categorys.objects.filter(for_footer=True)
	for_mid_part = Categorys.objects.filter(for_mid_part=True)
	is_option =  Categorys.objects.filter(is_option=True)
	products = Product.objects.all()
	product_images = ProductImage.objects.filter(is_main=True)
	location = Region.objects.all()
	context = {
		'for_header':for_header,
		'for_footer':for_footer,
		'for_mid_part':for_mid_part,
		'products':products,
		'is_option':is_option,
		'image':product_images,
		'location':location
	}
	return render(request,'index-2.html',context)
def product_detail(request,slug):
	product = get_object_or_404(Product,slug=slug)
	product_images = ProductImage.objects.all()
	for_header = Categorys.objects.filter(for_header=True)
	
	context = {
		'product':product,
		'images':product_images,
		'for_header':for_header,


	}
	return render(request,'post_detail.html',context)
from django.db.models import *
def category_products(request,slug):
	category = get_object_or_404(Categorys,slug=slug)
	products = Product.objects.filter(category=category)
	for_header = Categorys.objects.filter(for_header=True)
	is_option =  Categorys.objects.filter(is_option=True)
	location = Region.objects.all()
	product_images = ProductImage.objects.filter(is_main=True)
	user = CustomUser.objects.all()
	ctg = Categorys.objects.filter(is_option=True).annotate(nm=Count('product')).values('name','nm')
	context  = {
		'category':category,
		'products':products,
		'for_header':for_header,
		'is_option':is_option,
		'location':location,
		'ctg':ctg,
		'image':product_images,
		'user':user

	}
	return render(request,'category.html',context)	