from django.shortcuts import render
from categorys.models import *
from product.models import *
# Create your views here.
def main(request):
	for_header = Categorys.objects.filter(for_header=True)
	for_footer = Categorys.objects.filter(for_footer=True)
	for_mid_part = Categorys.objects.filter(for_mid_part=True)
	is_option =  Categorys.objects.filter(is_option=True)
	products = Product.objects.all()
	context = {
		'for_header':for_header,
		'for_footer':for_footer,
		'for_mid_part':for_mid_part,
		'products':products,
		'is_option':is_option
	}
	return render(request,'index-2.html',context)
