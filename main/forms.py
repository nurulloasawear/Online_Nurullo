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
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['class'] = "form-control"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': "your username",
            "password1": "your password1",
            "password2": "your password2"
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parollar mos kelmaydi")
        return password2

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['title','price','description','category','location','discount','condition','status','brand',]
		widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control input-md',
                'placeholder': 'Project Title'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control tg-select'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control input-md',
                'placeholder': 'Enter Price'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Project Description',
                'rows': 4
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }),
            'discount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Discount'
            }),
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Brand'
            }),
            'condition': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
class ContactForm(ModelForm):
	class Meta:
		model = ContactDetail
		exclude = ['product']
		widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control input-md',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control input-md',
                'placeholder': 'Last Name'
            }),
            'phone_n': forms.TextInput(attrs={
                'class': 'form-control input-md',
                'placeholder': 'Phone Number'
            }),
            'enter_address': forms.TextInput(attrs={
                'class': 'form-control input-md',
                'placeholder': 'Address'
            }),
            'country': forms.Select(attrs={
                'class': 'form-control tg-select'
            }),
            'state': forms.Select(attrs={
                'class': 'form-control tg-select'
            }),
            'city_area': forms.Select(attrs={
                'class': 'form-control tg-select'
            }),
        }
class ImageForm(ModelForm):
	class Meta:
		model = ProductImage
		exclude = ['product']
		widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file',})
       			 }
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
