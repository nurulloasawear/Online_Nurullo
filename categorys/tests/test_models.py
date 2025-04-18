from django.test import TestCase
from categorys.models import Categorys as Category
from categorys.models import Region, Brand


class CategoryModelTest(TestCase):
    def test_create_main_category(self):
        category = Category.objects.create(
            name='Uy-anjomlari',
            is_option=True,
            slug="Uy_anjomlari"
        )
        self.assertEqual(category.name, "Uy-anjomlari")
        self.assertTrue(category.is_option)
        self.assertEqual(category.slug, "Uy_anjomlari")
        self.assertIsNone(category.parent)

    def test_parent(self):
        category_e = Category.objects.create(
            name='Uy-anjomlari',
            is_option=True,
            slug="Uy_anjomlari"
        )

        sub_category = Category.objects.create(
            name="Chomich",
            is_option=False,
            slug="Chomich",
            parent=category_e
        )

        self.assertEqual(sub_category.parent, category_e)
class BrandModelTest(TestCase):
	def Test_create_region(self):
		region = Region.objects.create(country_id=1,name='Tashkent',sorting=9)
		self.assertEqual(region.name,'Tashkent')
		self.assertEqual(region.country_id,1)
		self.assertEqual(region.sorting,9)
class BrandTest(TestCase):
	def test_brand(self):
		brand = Brand.objects.create(name='Brand')
		self.assertEqual(brand.name,'Brand')
