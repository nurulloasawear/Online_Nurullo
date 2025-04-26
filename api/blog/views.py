from blog.models import Blog ,Comment
from .serializers import BlogSerializers,BlogCommentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins


# class BlogGenericAPIView(GenericAPIView):
# 	queryset = Blog.objects.all()
# 	serializer_class = BlogSerializers
	
# 	def get(self,request):
# 		blog = self.get_queryset()
# 		ser = self.get_serializer(blog,many=True)
# 		return Response(ser.data,status=status.HTTP_200_OK)
# 	def post(self,request):
# 		ser = self.get_serializer(data=request.data)
# 		if ser.is_valid():
# 			ser.save()
# 			return Response({"data":"upload with GenericAPIView"},status=status.HTTP_201_CREATED)

# class BlogDetailGenericAPIView(GenericAPIView):
# 	queryset = Blog.objects.all()
# 	serializer_class = BlogSerializers
	
# 	def get(self,request,pk):
# 		blog = self.get_object()
# 		ser = self.get_serializer(blog)
# 		return Response(ser.data,status=status.HTTP_200_OK)
# 	def put(self,request,pk):
# 		blog = self.get_object()
# 		ser = self.get_serializer(blog,data=request.data)
# 		if ser.is_valid():
# 			ser.save()
# 			return Response({"data":"upload with GenericAPIView"},status=status.HTTP_201_CREATED)
# 	def delete(self,request,pk):
# 		blog = self.get_object()
# 		blog.delte()
# 		return Response({"data":"deleted"})
class BlogMixinView(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializers

	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)
	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)


class BlogDetailMixinView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializers

	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)
	def put(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)
	def destroy(self,request,*args,**kwargs):
		self.create(request,*args,**kwargs)

class BlogCommentMixinView(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
	queryset = Comment.objects.all()
	serializer_class = BlogCommentSerializers

	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)
	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)


class BlogCommentDetailMixinView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
	queryset = Comment.objects.all()
	serializer_class = BlogCommentSerializers

	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)
	def put(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)
	def destroy(self,request,*args,**kwargs):
		self.create(request,*args,**kwargs)
