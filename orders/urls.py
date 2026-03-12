from django.urls import path
from . import views

urlpatterns = [
    # 0. The Root/Home Route (Defaults to Dashboard)
    path('', views.dashboard, name='dashboard'), 

    # 1. Collection endpoint
    path('api/orders/', views.order_list, name='order-list'),
    
    # 2. Analytics & Custom Filters
    path('api/orders/analytics/summary/', views.order_analytics, name='order-analytics'),
    path('api/orders/large/', views.large_orders, name='large-orders'),
    path('api/orders/date/<str:date_str>/', views.orders_by_date, name='orders-by-date'),
    path('api/customers/<str:customer_id>/orders/', views.customer_orders, name='customer-orders'),
    
    # 3. Detail endpoint
    path('api/orders/<str:pk>/', views.order_detail, name='order-detail'),
]