from django.urls import path
from .views import ProducDetail,Prouduct_color

urlpatterns = [
    path('product/<int:pk>',ProducDetail.as_view()),
    path("productcolor",Prouduct_color.as_view())
]


