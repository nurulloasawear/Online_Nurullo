from django.urls import path,include
from .views import product_con_img,product_detail

urlpatterns  = [
	path('nnn/',product_con_img),
	path('nnn/<int:pk>/',product_detail),

]