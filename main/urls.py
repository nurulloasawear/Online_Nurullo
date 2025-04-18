from django.urls import  path
from .views import main as maind
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',maind,name='main'),
    path('product/<slug:slug>/',product_detail,name="product_detail"),
    path('category/<slug:slug>/',category_products,name="category_products"),
    path('login',login_view,name="login"),
    path('logout',logout_views,name="logout"),
    path('register/',register_view,name="register"),
    path('post_add/',post_add,name="post_add"),
    # path('contact/',send_contact_email,name="contact")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
