from django.urls import  path
from .views import main as maind
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',maind),
    path('product/<slug:slug>/',product_detail,name="product_detail"),
    path('category/<slug:slug>/',category_products,name="category_products")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
