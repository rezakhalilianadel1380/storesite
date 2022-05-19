from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart,Cart_Item
from product.models import Features_price_effective
# Create your views here.

class Add_Cart(APIView):
    def post(self,request):
        quantity=request.POST.get('quantity')
        color=request.POST.get('color')
        color=Features_price_effective.objects.get(id=color)
        cart=Cart.objects.filter(user_id=request.user.id,is_paid=False)
        if cart.exists():
            cart=cart.first()
            if cart.cart_item_set.filter(color__id=color.id).exists():
                return Response({'payam':'already exists'})
            else:
                price=color.price+color.product.price
                Cart_Item.objects.create(color=color,product=color.product,quantity=quantity,cart=cart,price=price)
                return Response({'payam':'created'})
        else:
            cart=cart.create(user=request.user)
            price=color.price+color.product.price
            Cart_Item.objects.create(color=color,product=color.product,quantity=quantity,cart=cart,price=price)
            return Response({'payam':'created'})

        return Response({'okaay':'200'})

