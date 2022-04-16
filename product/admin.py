from django.contrib import admin
from .models import Product,Category,attr_product,Attribute_Category,Features_price_effective
# Register your models here.




admin.site.register(Product)
admin.site.register(Category)
admin.site.register(attr_product)
admin.site.register(Attribute_Category)
admin.site.register(Features_price_effective)