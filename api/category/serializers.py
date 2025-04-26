from rest_framework import serializers
from categorys.models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        fields = ['id','name','is_option','slug']
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id','name','sorting']
        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'