from django.contrib import admin
from demosite.models import Buyer
from demosite.models import Test
from demosite.models import Product

# Register your models here.
admin.site.register(Buyer)
admin.site.register(Test)
admin.site.register(Product)
