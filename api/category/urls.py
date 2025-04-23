from django.urls import path,include
from .views import get_list,multy,get,multypss

urlpatterns  = [
	path('',get_list),
	path('<int:pk>/',multy),
	path('region/',get),
	path('region/<int:pk>/',multypss)

]