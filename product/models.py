from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True,verbose_name='قیمت پایه ')
    quantity = models.IntegerField(null=True, blank=True,verbose_name='تعداد کل محصول ')
    image = models.ImageField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    product_type=models.BooleanField(default=False,verbose_name='نوع کالا /پیچیده ')
    brand_name_en=models.CharField(max_length=50,null=True)
    brand_name_fa=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.title

    def calculate_price(self):
        price_att=self.price_att.all().first()
        price=self.price+price_att.price
        return price


class Attribute_Category(models.Model):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title


class attr_product(models.Model):
    value = models.CharField(max_length=50)
    att_cat = models.ForeignKey(Attribute_Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title


class Features_price_effective(models.Model):
    name = models.CharField(
        choices=(('color', 'رنگ'), ('size', 'اندازه')), default='color', max_length=10)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='price_att')
    value = models.CharField(max_length=30)
    type = models.CharField(
        choices=(('D', 'Dropdown'), ('C', 'checkbox')), max_length=10)
    quantity = models.IntegerField()
    price = models.IntegerField()
    colorname=models.CharField(null=True,blank=True,max_length=50)

    def __str__(self):
        return self.colorname
