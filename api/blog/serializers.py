from rest_framework import serializers
from blog.models import Blog

class BlogSerializers(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = '__all__'
class BlogCommentSerializers(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = '__all__'
