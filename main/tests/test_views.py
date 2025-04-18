from django.test import TestCase, Client
from django.urls import reverse
from main.forms import *
from django.contrib.auth.models import User
from categorys.models import *
from product.models import *
from user.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
class Register_viewsTest(TestCase):
	def setUp(self):
		self.data =  {
			'username':'nurulloc',
			'email':'nurullodept@gmail.com',
			'password1':'Asatullayev05',
			'password2':'Asatullayev05'
		}
		self.data_1 =  {
			'username':'nurulloc',
			'email':'nueuadada@gmail.com',
			'password1':'Asatullayev05',
			'password2':'Asadasdasascdstullayev058'
		}
	def test_reg_views(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'register.html')
		self.assertIsInstance(response.context['form'],RegisterForm)

	def test_reg_valid(self):
		#POST sorovi  register uchun 
		response = self.client.post(reverse('register'),self.data)
		self.assertRedirects(response,reverse('login'))
		self.assertEqual(response.status_code,302)
		self.assertTrue(User.objects.filter(username='nurulloc').exists())
		# self.assertTrue(response.context['form'].is_valid())
	def test_reg_invalid(self):
		response = self.client.post(reverse('register'),self.data_1)
		self.assertEqual(response.status_code,200)
		self.assertFalse(response.context['form'].is_valid())
		self.assertTemplateUsed(response,'register.html')
		self.assertContains(response,"Parollar mos kelmaydi")



class Login_view_test(TestCase):
	def setUp(self):
		self.user = User.objects.create(username='nurullosss',password="nurullo123321")
		self.valid_data = {
            'login': 'Muhammad',
            'password': 'Nurullo2@2'
        }
		self.data_1 = {'login':'admingg','password':'ff4g522h53g3g'}
	def test_login_get(self):
		response = self.client.get(reverse('login'))
		self.assertTemplateUsed(response,'login.html')
		self.assertEqual(response.status_code,200)
		self.assertIsInstance(response.context['form'],LoginForm)
	def test_login_post_valid(self):
		response = self.client.post(reverse('login'),self.valid_data)
		# self.assertEqual(response.status_code,302)
		# self.assertRedirects(response,response('main'))
		# self.assertTrue(User.objects.filter(self.data))
class logout_view_test(TestCase):
	def test_logout(self):
		url = self.client.get(reverse('logout'))
		self.assertRedirects(url,reverse('main')) 


from django.db.models import Prefetch
import tempfile
from django.conf import settings
import os
import shutil
from decimal import Decimal

# @override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class MainViewTest(TestCase):
    def setUp(self):
        # Model obyektlarini yaratish
        self.country = country.objects.create(name="Uzbekistan")
        self.region = Region.objects.create(
            country_id=self.country,
            name="Toshkent",
            sorting=1
        )
        self.brand = Brand.objects.create(name="Test Brand")
        # User va Product yaratish
        self.user = User.objects.create_user(
            username="nurullosss",
            password="nurullo123321"
        )
        self.custom_user = CustomUser.objects.create(
            user=self.user,
            first_name="Test",
            phone_number="+998901234567"
        )
        test_image = SimpleUploadedFile(
            name="test.jpg",
            content=b"file_content",
            content_type="image/jpeg"
        )

        self.is_option = Categorys.objects.create(
        	name="multy",
        	image=test_image,
        	for_header=True,
        	is_option=True,
        	for_footer=True,
        	for_mid_part=True,
        	slug="header_Ts"
        	)
        self.product = Product.objects.create(
            title="Test Product",
            price=Decimal("100.30"),
            description="Test description",
            category=self.is_option,
            location=self.region,
            brand=self.brand,
            User=self.custom_user,
            discount=10,
            condition=1,
            status=1
        )
        
        # Rasm yaratish va saqlash
        test_image = SimpleUploadedFile(
            name="test.jpg",
            content=b"file_content",
            content_type="image/jpeg"
        )
        self.product_image = ProductImage.objects.create(
            product=self.product,
            image=test_image,
            is_main=True
        )
        # self.is_option = Categorys.objects.create(
        # 	name="multy",
        # 	image=test_image,
        # 	for_header=True,
        # 	is_option=True,
        # 	for_footer=True,
        # 	for_mid_part=True,
        # 	slug="header_Ts"
        # 	)
    def test_get_main(self):
        	response = self.client.get(reverse('main'))
        	self.assertTemplateUsed(response,'index-2.html')
        	self.assertEqual(response.status_code,200)
        	context = response.context
        	self.assertIn('for_header',context)
        	self.assertIn('for_footer',context)
        	self.assertIn('is_option',context)
        	self.assertIn('for_mid_part',context)
        	#
        	self.assertEqual(context['for_header'].first().name,'multy')
        	self.assertEqual(len(context['is_option']),1)
        	self.assertEqual(list(context['for_footer'].values_list('name',flat=True)),["multy"])
        	self.assertEqual(context['location'].count(),1)
        	self.assertEqual(context['location'].first().name,'Toshkent')
        	#
        	self.assertEqual(context['products'].count(),1)
        	product_from_context = context['products'].first()
        	self.assertTrue(hasattr(product_from_context,'main_images'))
        	self.assertEqual(len(product_from_context.main_images),1)
        	self.assertTrue(hasattr(product_from_context, 'main_images'))
	        self.assertEqual(len(product_from_context.main_images), 1)
	        self.assertTrue(product_from_context.main_images[0].is_main)
	        # self.assertTrue(product_from_context.main_images[0].image.name.endswith("test.jpg"))

	        # Verify discount logic
	        expected_price = Decimal("100.30") * (1 - Decimal("0.10"))  # 100.30 - 10% = 90.27
	        self.assertEqual(product_from_context.price, expected_price)
	        self.assertEqual(product_from_context.slug, slugify("Test Product"))

    def test_get_main_empty_data(self):
        # Clear the database
        country.objects.all().delete()
        Region.objects.all().delete()
        Categorys.objects.all().delete()
        Product.objects.all().delete()
        ProductImage.objects.all().delete()
        Brand.objects.all().delete()
        User.objects.all().delete()
        CustomUser.objects.all().delete()

        # Send GET request to the view
        response = self.client.get(reverse('main'))

        # Check status code and template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index-2.html')

        # Verify context data (should be empty)
        context = response.context
        self.assertEqual(context['for_header'].count(), 0)
        self.assertEqual(context['for_footer'].count(), 0)
        self.assertEqual(context['for_mid_part'].count(), 0)
        self.assertEqual(context['is_option'].count(), 0)
        self.assertEqual(context['products'].count(), 0)
        self.assertEqual(context['location'].count(), 0)

    def test_get_main_no_images(self):
        ProductImage.objects.all().delete()

        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index-2.html')

        context = response.context
        self.assertEqual(context['products'].count(), 1)
        product_from_context = context['products'].first()
        self.assertTrue(hasattr(product_from_context, 'main_images'))
        self.assertEqual(len(product_from_context.main_images), 0)
# Yangi test sinflari
class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.test_media_root = os.path.join(settings.BASE_DIR, 'media_test')
        if not os.path.exists(self.test_media_root):
            os.makedirs(self.test_media_root)
        settings.MEDIA_ROOT = self.test_media_root

        self.country = country.objects.create(name="Uzbekistan")
        self.region = Region.objects.create(country_id=self.country, name="Toshkent", sorting=1)
        self.brand = Brand.objects.create(name="Test Brand")
        self.header_category = Categorys.objects.create(
            name="Header Category", slug="header", for_header=True
        )
        self.user = User.objects.create_user(username="nurullosss", password="nurullo123321")
        self.custom_user = CustomUser.objects.create(
            user=self.user, first_name="Test", phone_number="+998901234567"
        )
        self.product = Product.objects.create(
            title="Test Product",
            slug=slugify("Test Product"),
            price=Decimal("100.30"),
            description="Test description",
            category=self.header_category,
            location=self.region,
            brand=self.brand,
            User=self.custom_user,
            discount=10,
            condition=1,
            status=1
        )
        test_image = SimpleUploadedFile(
            name="test.jpg", content=b"file_content", content_type="image/jpeg"
        )
        self.product_image = ProductImage.objects.create(
            product=self.product, image=test_image, is_main=True
        )

    def tearDown(self):
        if os.path.exists(self.test_media_root):
            shutil.rmtree(self.test_media_root)

    def test_product_detail_valid_slug(self):
        response = self.client.get(reverse('product_detail', args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        context = response.context
        self.assertIn('product', context)
        self.assertIn('images', context)
        self.assertIn('for_header', context)
        self.assertEqual(context['product'], self.product)
        self.assertEqual(context['images'].count(), 1)
        self.assertEqual(context['images'].first().image.name, self.product_image.image.name)
        self.assertEqual(context['for_header'].count(), 1)
        self.assertEqual(context['for_header'].first().name, "Header Category")

    def test_product_detail_invalid_slug(self):
        response = self.client.get(reverse('product_detail', args=['invalid-slug']))
        self.assertEqual(response.status_code, 404)

class PostAddViewTest(TestCase):
    def setUp(self):
        self.test_media_root = os.path.join(settings.BASE_DIR, 'media_test')
        if not os.path.exists(self.test_media_root):
            os.makedirs(self.test_media_root)
        settings.MEDIA_ROOT = self.test_media_root

        self.country = country.objects.create(name="Uzbekistan")
        self.region = Region.objects.create(country_id=self.country, name="Toshkent", sorting=1)
        self.brand = Brand.objects.create(name="Test Brand")
        self.category = Categorys.objects.create(
            name="Test Category", slug="test-category", for_header=True
        )
        self.user = User.objects.create_user(username="nurullosss", password="nurullo123321")
        self.custom_user = CustomUser.objects.create(
            user=self.user, first_name="Test", phone_number="+998901234567"
        )

    def tearDown(self):
        if os.path.exists(self.test_media_root):
            shutil.rmtree(self.test_media_root)

    def test_post_add_get(self):
        self.client.login(username="nurullosss", password="nurullo123321")
        response = self.client.get(reverse('post_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_add.html')
        context = response.context
        self.assertIn('form', context)
        self.assertIn('form_con', context)
        self.assertIn('form_img', context)
        self.assertIsInstance(context['form'], ProductForm)
        self.assertIsInstance(context['form_con'], ContactForm)
        self.assertIsInstance(context['form_img'], ImageForm)

    def test_post_add_valid_post(self):
        self.client.login(username="nurullosss", password="nurullo123321")
        test_image = SimpleUploadedFile(
            name="test.jpg", content=b"file_content", content_type="image/jpeg"
        )
        data = {
            'title': "New Product",
            'price': "200.50",
            'description': "New description",
            'category': self.category.id,
            'location': self.region.id,
            'brand': self.brand.id,
            'discount': 5,
            'condition': 1,
            'status': 1,
            # ContactForm uchun maydonlar (agar mavjud bo'lsa, moslashtiring)
            'phone_number': "+998901234567",
            # ImageForm uchun maydonlar
            'is_main': True,
        }
        files = {'image': test_image}
        response = self.client.post(reverse('post_add'), data=data, files=files)
        # self.assertEqual(response.status_code, 302)  # Redirect to 'main'
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(ProductImage.objects.count(), 1)
        product = Product.objects.first()
        self.assertEqual(product.title, "New Product")
        self.assertEqual(product.User, self.custom_user)
        image = ProductImage.objects.first()
        self.assertTrue(image.image.name.endswith("test.jpg"))

    def test_post_add_invalid_post(self):
        self.client.login(username="nurullosss", password="nurullo123321")
        data = {
            'title': "",  # Bo'sh maydon, forma xato bo'ladi
            'price': "invalid",  # Noto'g'ri format
        }
        response = self.client.post(reverse('post_add'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_add.html')
        self.assertFalse(response.context['form'].is_valid())
        self.assertFalse(response.context['form_con'].is_valid())
        self.assertFalse(response.context['form_img'].is_valid())

class CategoryProductsViewTest(TestCase):
    def setUp(self):
        self.test_media_root = os.path.join(settings.BASE_DIR, 'media_test')
        if not os.path.exists(self.test_media_root):
            os.makedirs(self.test_media_root)
        settings.MEDIA_ROOT = self.test_media_root

        self.country = country.objects.create(name="Uzbekistan")
        self.region = Region.objects.create(country_id=self.country, name="Toshkent", sorting=1)
        self.brand = Brand.objects.create(name="Test Brand")
        self.category = Categorys.objects.create(
            name="Test Category", slug="test-category", for_header=True, is_option=True
        )
        self.user = User.objects.create_user(username="nurullosss", password="nurullo123321")
        self.custom_user = CustomUser.objects.create(
            user=self.user, first_name="Test", phone_number="+998901234567"
        )
        self.product = Product.objects.create(
            title="Test Product",
            price=Decimal("100.30"),
            description="Test description",
            category=self.category,
            location=self.region,
            brand=self.brand,
            User=self.custom_user,
            discount=10,
            condition=1,
            status=1
        )
        test_image = SimpleUploadedFile(
            name="test.jpg", content=b"file_content", content_type="image/jpeg"
        )
        self.product_image = ProductImage.objects.create(
            product=self.product, image=test_image, is_main=True
        )

    def tearDown(self):
        if os.path.exists(self.test_media_root):
            shutil.rmtree(self.test_media_root)

    def test_category_products_valid_slug(self):
        response = self.client.get(reverse('category_products', args=[self.category.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')
        context = response.context
        self.assertIn('category', context)
        self.assertIn('products', context)
        self.assertIn('for_header', context)
        self.assertIn('is_option', context)
        self.assertIn('location', context)
        self.assertIn('ctg', context)
        self.assertIn('images', context)
        self.assertEqual(context['category'], self.category)
        self.assertEqual(context['products'].paginator.count, 1)
        self.assertEqual(context['for_header'].count(), 1)
        self.assertEqual(context['is_option'].count(), 1)
        self.assertEqual(context['location'].count(), 1)
        self.assertEqual(context['ctg'].count(), 1)
        self.assertEqual(context['images'].count(), 1)

    def test_category_products_pagination(self):
        # Qo'shimcha mahsulot qo'shish
        Product.objects.create(
            title="Second Product",
            price=Decimal("50.00"),
            description="Second description",
            category=self.category,
            location=self.region,
            brand=self.brand,
            User=self.custom_user,
            condition=1,
            status=1
        )
        response = self.client.get(reverse('category_products', args=[self.category.slug]) + '?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].paginator.per_page, 1)
        self.assertEqual(response.context['products'].object_list.count(), 1)

    def test_category_products_invalid_slug(self):
        response = self.client.get(reverse('category_products', args=['invalid-slug']))
        self.assertEqual(response.status_code, 404)