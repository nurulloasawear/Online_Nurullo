from django.test import TestCase, Client
from django.urls import reverse
from categorys.models import Region  
from categorys.forms import RegionForm
from product.models import country

class RegionViewTest(TestCase):
	def setUp(self):
		# Countryga yengi obyekt qoshamz
		self.country = country.objects.create(name="Qozoqiston")
		# Test REgion modeli
		self.region = Region.objects.create(
			country_id = self.country,
			name = "Almata",
			sorting = 11
			)
		self.data = {
		'country_id':1,
		'name':'Qashqadaryo',
		'sorting':33
		}
		self.data_1 = {
		'country_id':1,
		'name':'',
		'sorting':33
		}
		def test_region_view_get(self):
			#Get so'rov tesst
			response = self.client.get(reverse('region'))
			#statud kodini tekshish
			self.assertEqual(response.status_code,200)
			#Qaysi htmlni django yuborvotganini tekshiramz
			self.assertTemplateUsed(response,'region.html')
			# ctx ichida form yuborganmi yoqmi shuni isinstance orqali tekshrsa boladi
			self.assertIsInstance(response.context['form'],RegionForm)
			#Formda country_id uchun to'gri kevotganini tekshirish uchun  queryset bunga yordam beradi ?
			self.assertIn(self.country,response.context['form'].fields['country_id'].queryset)
		def test_region_viev_post_valid(self):
			#Togri post yuborlshi uchun oldindan data tayor bolish kerak
			# man esa setUp da oldinda tayorlab oganman
			response = self.client.post(reverse('region'),self.data)
			# 302 status_code kevotganini tekshiramz va URl  holatini teksshiramz
			self.assertEqual(response.status_code,302)	
			self.assertRedirects(response,reverse('region'))
			#malumot saqlandimi yomi tekshirish
			self.assertTrue(Region.objects.filter('Qashqadaryo').exists())

		def test_region_viev_post_invalid(self):
			#Notogri post yuborlayotganinig tekshirmoqchiman uning uchun notori malumotni oldindan tayorlavoganman
			response = self.client.post(reverse('region'),data)
			# 200 kevotganini tekshirsh  chunki forma notori bolsa qayta yuklanadi 200 korsatish kerak
			self.assertTemplateUsed(response,'region.html')
			#form  togrimi yoki yoqmi is_valid orqali tekshirsh false qaytishi kutilmoqda chunki notogri malumot berilgan
			self.assertFalse(response.context['form'].is_valid())
			# Malumot saqlanmaganligini tekshirsh
			self.assertFalse(Region.objects.filter('Qashqadaryo').exists())
		def test_region_view_form_display(self):
			#buyoda shunchaki get qivomz
			response = self.client.get(reverse(region))
			#formani ichida uzbekiston kelayotmi yoki yoqmi tekshirish chunki country_id boglangan buyerdan chiqayotimi yoki yoqligini bilidh kerak
			self.assertContains(response,"Uzbekistan")
