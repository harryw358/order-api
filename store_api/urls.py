from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView,  SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # This pulls in all routes from orders/urls.py
    path('', include('orders.urls')),

    # Schema & Documentation UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc UI:
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]