from django.urls import path,include
from .views import *

urlpatterns  = [
	path('',CategorysView.as_view()),
	path('<int:pk>/',CategoryspkView.as_view()),
	path('region/',RegionView.as_view()),
	path('region/<int:pk>/',RegionpkView.as_view()),
	path('brand/',Brands.as_view()),
	path('brand/<int:pk>/',BrandPut.as_view())
]