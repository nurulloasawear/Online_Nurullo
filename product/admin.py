from django.contrib import admin
from .models import *
admin.site.register(Product)
# Register your models here.
admin.site.register(ProductImage)

admin.site.register(Area)
admin.site.register(country)
admin.site.register(ContactDetail)


