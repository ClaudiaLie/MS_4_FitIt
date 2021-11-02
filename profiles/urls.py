from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('add_goal', views.add_goal, name='add_goal'),
    path('edit_goal/<goal_id>', views.edit_goal, name='edit_goal'),
]
