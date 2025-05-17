from  django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
	TokenVerifyView
	)
urlpatterns = [
	path('login/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
	path('login/token/refresh/',TokenRefreshView.as_view(),name='token_refresh4'),
	path('login/token/verify/',TokenVerifyView.as_view(),name='token_verify'),
	path('login/',login,name='token_verify'),

]