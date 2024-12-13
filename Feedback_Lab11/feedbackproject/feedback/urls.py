from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('items/', views.feedback_list, name='feedback_list'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
]