from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Product
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




