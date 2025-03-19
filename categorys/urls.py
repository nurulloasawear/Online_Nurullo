from django.urls import path
from .views  import Region

urlpatterns = [
	path('',Region,name='Region')
]

