from django.urls import path,include

urlpatterns = [
	path('category/',include('api.category.urls')),
	path('product/',include('api.product.urls'))

]