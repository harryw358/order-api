from django.urls import path
from . import views

urlpatterns = [
    path('api/orders/', views.order_list, name='order-list'),
    path('api/orders/<str:pk>/', views.order_detail, name='order-detail'),
]