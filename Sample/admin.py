from django.contrib import admin
from .models import Companies,Product,Purchase_Order

# Register your models here.
admin.site.register(Companies)
admin.site.register(Product)
admin.site.register(Purchase_Order)