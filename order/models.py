from django.db import models
from django.contrib.auth.models import User
from product.models import Features_price_effective
from product.models import Product
# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    is_paid=models.BooleanField(default=False)
    payment_date=models.DateTimeField(blank=True,null=True,verbose_name='تاریخ پرداخت')
    tracking_code=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.user.username


class Cart_Item(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()
    color=models.ForeignKey(Features_price_effective,null=True,blank=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.IntegerField()

    
    def __str__(self) -> str:
        return f"{self.product.title}    |    {self.color.colorname}"