from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Features_price_effective
from order.models  import Cart, Cart_Item
# Create your views here.



class ProducDetail(DetailView):
    model = Product
    template_name = "detail_view.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_object(self):
        request = self.request
        productid = self.kwargs.get('pk')
        product=Product.objects.get(id=productid)
        return product



class Prouduct_color(APIView):
    def get(self, request):
        id=request.GET.get('color')
        color=Features_price_effective.objects.get(id=id)
        price=color.price+color.product.price
        cart=Cart.objects.filter(user_id=request.user.id,is_paid=False)
        if  cart.exists():
            cart=cart.first()
            if  cart.cart_item_set.filter(color__id=id).exists():
                return Response({'price':price})
        return Response({'price':price})




