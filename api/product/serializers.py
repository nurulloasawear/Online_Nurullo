from product.models import * 
from rest_framework import serializers as serializer


		
class ProductViewSerializer(serializer.ModelSerializer):
	class Meta:
		model = ProductView
		fields = '__all__'
class ProductImageSerializer(serializer.ModelSerializer):
	class Meta:
		model = ProductImage
		exclude = ['product']
class AreaSerializer(serializer.ModelSerializer):
	class Meta:
		model = Area
		fields = '__all__'
class ContactDetailSerializer(serializer.ModelSerializer):
	class Meta:
		model = ContactDetail
		exclude = ['product']
class ProductMultySerializer(serializer.ModelSerializer):
	contactinfo = ContactDetailSerializer(read_only=True)
	productimage = ProductImageSerializer(read_only=True)
	class Meta:
		model = Product
		exclude = ['createdat','update_at']

	def create(self, validated_data):
		contact_data = validated_data.pop('contact_info')
		image_data = validated_data.pop('image')
		user = self.context['request'].user.profile

		product = Product.objects.create(User=user,**validated_data)
		ContactDetail.objects.create(product=product,**contact_data)
		ProductImage.objects.create(product=product,**image_data)
		