from django.shortcuts import render,get_object_or_404,redirect
from categorys.models import *
from product.models import *
from user.models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
# from django.contrib.mail import send_mail
from django.conf import settings
# Create your views here.

def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			form.add_error(None,"Toliq va hatolarsiz toldiring!")
	context = {
     'form':form
		}
	return render(request,'register.html',context)			

def login_view(request):
	form = LoginForm()
	url = request.GET.get('url','main')
	print(url)
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['login']
			password = form.cleaned_data['password']
			user = authenticate(request,username=username,password=password)
			if user is not None :
				login(request,user)
				return redirect(url)
			else:
				form.add_error(None,"Login yoki oarol notogiri")
		else:
			form = LoginForm()
	return render(request,'login.html',{'form':form})

def logout_views(request):
	logout(request)
	return redirect('main')
def main(request):
	for_header = Categorys.objects.filter(for_header=True)
	for_footer = Categorys.objects.filter(for_footer=True)
	for_mid_part = Categorys.objects.filter(for_mid_part=True)
	is_option =  Categorys.objects.filter(is_option=True)
	# products = Product.objects.all()
	products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
	location = Region.objects.all()
	context = {
		'for_header':for_header,
		'for_footer':for_footer,
		'for_mid_part':for_mid_part,
		'products':products,
		'is_option':is_option,
		'location':location,
		# 'user':user
	}
	return render(request,'index-2.html',context)
def product_detail(request,slug):
	product = get_object_or_404(Product,slug=slug)
	product_images = ProductImage.objects.filter(product=product.id)
	for_header = Categorys.objects.filter(for_header=True)
	
	context = {
		'product':product,
		'images':product_images,
		'for_header':for_header,


	}
	return render(request,'post_detail.html',context)

def post_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form_con = ContactForm(request.POST)
        form_img = ImageForm(request.POST, request.FILES)
        print(form)
        print(form_con)
        print(form_img)
        print(form.is_valid(),form_con.is_valid(),form_img.is_valid())
        print(request.FILES)
        if form.is_valid() and form_con.is_valid() and form_img.is_valid():#
            product = form.save(commit=False)
            product.User = request.user.profile
            product.save()
            con = form_con.save(commit=False)
            con.product = product
            con.save()
            f = form_img.save(commit=False)
            f.product = product
            f.save()
            # print("Error-form:",product)
            # print("Error-form_con",con)
            # print("Error-form_img",f)

            return redirect('main')
    else:
        form = ProductForm()
        form_con = ContactForm()
        form_img = ImageForm()
    return render(request, 'post_add.html', {
        'form': form,
        'form_con': form_con,
        'form_img': form_img
    })
from django.core.paginator import Paginator
from django.db.models import *
def category_products(request,slug):
	category = get_object_or_404(Categorys,slug=slug)
	product = Product.objects.filter(category=category)
	paginator  = Paginator(product,1)
	pag_req = request.GET.get("page")
	page_obj =  paginator.get_page(pag_req)
	for_header = Categorys.objects.filter(for_header=True)
	is_option =  Categorys.objects.filter(is_option=True)
	location = Region.objects.all()
	product_images = ProductImage.objects.exclude(is_main=False)
	user = CustomUser.objects.all()
	ctg = Categorys.objects.filter(is_option=True).annotate(nm=Count('product')).values('name','nm')
	context  = {
		'category':category,
		'products':page_obj,
		'for_header':for_header,
		'is_option':is_option,
		'location':location,
		'ctg':ctg,
		'images':product_images,
		# 'user':user

	}
	return render(request,'category.html',context)	
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.conf import settings
# from .forms import ContactForm

# def send_contact_email(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             full_message = f"From: {name} <{email}>\n\n{message}"

#             send_mail(
#                 subject="Yangi xabar websaytda",
#                 message=full_message,
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=['nurullostepn3@gmail.com'],
#                 fail_silently=False
#             )

#             return redirect('main')  # Xabarning yuborilganidan so'ng asosiy sahifaga qaytish
#     else:
#         form = ContactForm()

#     return render(request, 'contact.html', {'form': form})
