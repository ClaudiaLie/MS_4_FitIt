from django.urls import path
from . import views

urlpatterns = [
    path('', views.prices, name='prices'),
]
