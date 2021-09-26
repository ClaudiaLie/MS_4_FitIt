from django.urls import path
from . import views


urlpatterns = [
    path('', views.gym_classes, name='gym_classes'),
    path('body_building', views.body_building, name='body_building'),
    path('dance', views.dance, name='dance'),
    path('yoga', views.yoga, name='yoga'),
]
