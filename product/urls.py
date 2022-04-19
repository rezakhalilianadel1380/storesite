from django.urls import path
from .views import ProducDetail

urlpatterns = [
    path('product/<int:pk>',ProducDetail.as_view()),

]


