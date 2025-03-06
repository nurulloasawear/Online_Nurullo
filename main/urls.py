from django.urls import  path
from .views import main as maind
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',maind)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
