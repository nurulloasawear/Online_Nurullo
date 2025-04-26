from django.shortcuts import render,get_object_or_404
from categorys.models import *
from categorys.models import Brand 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status	
from rest_framework.views import APIView as ApiView
from .serializers import PostSerializer as CtSerializer,RegionSerializer,BrandSerializer

# @api_view(['GET', 'POST']) 
# def get_list(request):
# 	if request.method == 'GET':
# 		category = Categorys.objects.all()
# 		data = CtSerializer(category,many=True)
# 		print(data.data)
# 		return Response({"data":data.data})
# 	elif request.method == 'POST':
# 		serializer = CtSerializer(data=request.data)
# 		print(serializer,serializer.is_valid())
# 		if serializer.is_valid():
# 			res = serializer.save()
# 			print(res)
# 			return Response({'data':'succes'},status=status.HTTP_201_CREATED)
# @api_view(["GET","PUT","DELETE"])
# def multy(request,pk):
# 	try:
# 		category = Categorys.objects.get(pk=pk)
# 	except Categorys.DoesNotExists:
# 		return Response({'error':'Topilmadi'})
# 	if request.method == "GET":
# 		ser = CtSerializer(category)
# 		return Response(ser.data)
# 	elif request.method == "PUT":
# 		ser = CtSerializer(category,data=request.data)
# 		print(ser.is_valid())
# 		if ser.is_valid():
# 			ser.save()
# 			print(ser)
# 			return Response({"data":"updateted"})


# @api_view(['GET', 'POST']) 
# def get(request):
# 	if request.method == 'GET':
# 		region = Region.objects.all()
# 		data = RegionSerializer(region,many=True)
# 		print(data.data)
# 		return Response({"data":data.data})
# 	elif request.method == 'POST':
# 		serializer = RegionSerializer(data=request.data)
# 		print(serializer,serializer.is_valid())
# 		if serializer.is_valid():
# 			res = serializer.save()
# 			print(res)
# 			return Response({'data':'succes'},status=status.HTTP_201_CREATED)
# @api_view(["GET", "PUT"])
# def multypss(request, pk):
# 	try:
# 		region = Region.objects.get(pk=pk)
# 	except Region.DoesNotExist:
# 		return Response({'error': 'Topilmadi'}, status=status.HTTP_404_NOT_FOUND)

# 	if request.method == "GET":
# 		ser = RegionSerializer(region)
# 		return Response(ser.data)

# 	elif request.method == "PUT":
# 		ser = RegionSerializer(region, data=request.data)
# 		if ser.is_valid():
# 			ser.save()
# 			return Response({"data": "updated"})
# 		return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class Brands(ApiView):
	def get(self,request):
		brand = Brand.objects.all()
		ser = BrandSerializer(brand,many=True)
		return Response(ser.data,status=status.HTTP_200_OK)
	def post(self,request):
		ser = BrandSerializer(data=request.data)
		if ser.is_valid():
			ser.save()
			return Response({'data':'succes'},status=status.HTTP_201_CREATED)
		return Response({'data':'fiel'},status=status.HTTP_400_BAD_REQUEST)
class BrandPut(ApiView):
	def get_o(self,pk):
		try:
			self.brand = Brand.objects.get(pk=pk)
			return self.brand
		except brand.DoesNotExist:
			return Response({'error': 'Topilmadi'}, status=status.HTTP_404_NOT_FOUND)

	def get(self,request,pk):
		ser = BrandSerializer(self.get_o(pk),status=status.HTTP_200_OK)
		return Response(ser,status=status.HTTP_200_OK)
	def put(self,request,pk):
		ser = BrandSerializer(self.get_o(pk),data=request.data)
		if ser.is_valid():
			ser.save()
		return Response({"data": "updated"})
	def delete(self,request,pk):
		self.get_o(pk).delete()
		return {"No":"Content"}	
class RegionView(ApiView):
	def get(self,request):
		region = Region.objects.all()
		ser = RegionSerializer(region,many=True) 
		return Response(ser.data,status=status.HTTP_200_OK)
	def post(self,request):
		ser = BrandSerializer(data=request.data)
		if ser.is_valid():
			ser.save()
			return Response({'data':'succes'},status=status.HTTP_201_CREATED)
		return Response({'data':'unupload'},status=status.HTTP_400_BAD_REQUEST)
class RegionpkView(ApiView):
	def scan(self,pk):
		self.t = get_object_or_404(Region,pk=pk)
		return self.t
	def get(self,request,pk):
		self.scan(pk)
		ser = RegionSerializer(self.t)
		return Response(ser.data,status=status.HTTP_200_OK)
	def put(self,request,pk):
		self.scan(pk)
		ser = RegionSerializer(self.t,data=request.data)
		if ser.is_valid():
			ser.save()
			return Response({'data':'succes'},status=status.HTTP_200_OK)
		return Response({'data':'unupload','errors':ser.errors},status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request,pk):
		self.scan(pk).delete()
		return Response({"data":"deleted"},status=status.HTTP_204_NO_CONTENT)
class CategorysView(ApiView):
	def get(self,request):
		model = Categorys.objects.all()
		ser = CtSerializer(model,many=True)
		return Response(ser.data,status=status.HTTP_200_OK)
	def post(self,request):
		ser = CtSerializer(data=request.data)
		if ser.is_valid():
			ser.save()
			return Response({'data':'created'},status=status.HTTP_201_CREATED)
		return Response({"errors":ser.errors})
class CategoryspkView(ApiView):
	def dry(self,pk):
		self.pk = get_object_or_404(Categorys,pk=pk)
		return self.pk 
	def get(self,request,pk):
		self.dry(pk)
		ser = CtSerializer(self.pk)
		return Response(ser.data,status=status.HTTP_200_OK)
	def put(self,request,pk):
		self.dry(pk)
		ser = CtSerializer(self.pk,data=request.data)
		if ser.is_valid():
			ser.save()
			return Response({"data":"updateted"},status=status.HTTP_200_OK)
		else:
			return Response({"date":"unupload","erros":ser.errors},status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request,pk):
		self.dry(pk).delete()
		return Response({"data":"delted"},status=status.HTTP_204_NO_CONTENT)

