from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from product.models import Product,ContactDetail,ProductImage
class LoginForm(forms.Form):
	login = forms.CharField(max_length=30,label="Login",widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Password")
class RegisterForm(UserCreationForm):
	email = forms.EmailField(
		label="your email",
		widget=forms.EmailInput(attrs={'class':'form-control'})
		)
	def __init__(self,*args,**kwargs):
		super(RegisterForm,self).__init__(*args,**kwargs)
		self.fields['password1'].widget.attrs['class'] = "form-control"
		self.fields['password2'].widget.attrs['class'] = "form-control"

	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		labels = {
			'username':"your username",
			"password1":"your password1",
			"password2":"your password2"

		}
		widgets = {
		'username':forms.TextInput(attrs={'class':'form-control'}),
		}
class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['title','price','description','category','location','brand','discount','condition','status']
class ContactForm(ModelForm):
	class Meta:
		model = ContactDetail
		fields = '__all__'
class imageForm(ModelForm):
	class Meta:
		model = ProductImage
		fields = ['image','is_main']
