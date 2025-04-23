from django.shortcuts import render
from categorys.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer as CtSerializer,RegionSerializer
@api_view(['GET', 'POST']) 
def get_list(request):
	if request.method == 'GET':
		category = Categorys.objects.all()
		data = CtSerializer(category,many=True)
		print(data.data)
		return Response({"data":data.data})
	elif request.method == 'POST':
		serializer = CtSerializer(data=request.data)
		print(serializer,serializer.is_valid())
		if serializer.is_valid():
			res = serializer.save()
			print(res)
			return Response({'data':'succes'},status=status.HTTP_201_CREATED)
@api_view(["GET","PUT","DELETE"])
def multy(request,pk):
	try:
		category = Categorys.objects.get(pk=pk)
	except Categorys.DoesNotExists:
		return Response({'error':'Topilmadi'})
	if request.method == "GET":
		ser = CtSerializer(category)
		return Response(ser.data)
	elif request.method == "PUT":
		ser = CtSerializer(category,data=request.data)
		print(ser.is_valid())
		if ser.is_valid():
			ser.save()
			print(ser)
			return Response({"data":"updateted"})
@api_view(['GET', 'POST']) 
def get(request):
	if request.method == 'GET':
		region = Region.objects.all()
		data = RegionSerializer(region,many=True)
		print(data.data)
		return Response({"data":data.data})
	elif request.method == 'POST':
		serializer = RegionSerializer(data=request.data)
		print(serializer,serializer.is_valid())
		if serializer.is_valid():
			res = serializer.save()
			print(res)
			return Response({'data':'succes'},status=status.HTTP_201_CREATED)
@api_view(["GET", "PUT"])
def multypss(request, pk):
	try:
		region = Region.objects.get(pk=pk)
	except Region.DoesNotExist:
		return Response({'error': 'Topilmadi'}, status=status.HTTP_404_NOT_FOUND)

	if request.method == "GET":
		ser = RegionSerializer(region)
		return Response(ser.data)

	elif request.method == "PUT":
		ser = RegionSerializer(region, data=request.data)
		if ser.is_valid():
			ser.save()
			return Response({"data": "updated"})
		return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
