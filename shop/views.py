from turtle import title
from unicodedata import category
from django.shortcuts import render, HttpResponse
from product.models import Product, Category, attr_product, Attribute_Category
# Create your views here.


def homepage(request):
    products = Product.objects.all()
    product=Product.objects.get(id=1)
    category=product.category.all().first()
    attri_cat= category.attribute_category_set.all()
    color= attri_cat.filter(title='رنگ')
    context = {
        'product': products,
        'pro':product,
    }
    return render(request, 'homepage.html', context)
