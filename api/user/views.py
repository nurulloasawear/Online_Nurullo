from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET', 'POST']) 
def login(request):
	username = request.data.get('username',None)
	password = request.data.get('password',None)
	user =  authenticate(username=username,password=password)
	if user:
		token,_ = Token.objects.get_or_create(user=user)
		return Response({"Token":token.key},status=status.HTTP_200_OK)



