from django.urls import include, path
from .views import Add_Cart

urlpatterns = [
    path('api/cart/add',Add_Cart.as_view()),
]