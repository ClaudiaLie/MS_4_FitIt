from django.urls import path
from . import views

urlpatterns = [
    path('', views.gym_classes, name='gym_classes'),
]
