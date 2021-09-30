from django.urls import path
from .views import *

urlpatterns = [
    # url to home page
    path('product/',ProductListHandler.as_view()),
    path('product/<str:pk>/',ProductHandler.as_view()),
]