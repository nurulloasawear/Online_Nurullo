from django.urls import path,include
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter
routers = DefaultRouter()
routers.register(r'',ProductViewSet)

urlpatterns  = [
	path("set/",include(routers.urls)),
	# path('nnn/',product_con_img),
	# path('nnn/<int:pk>/',product_detail),

]