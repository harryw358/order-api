from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    # Include the calculated property as a read-only field
    line_total = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = ['id', 'stock_code', 'description', 'quantity', 'price', 'line_total']

class OrderSerializer(serializers.ModelSerializer):
    # Nested serializer to include all items inside the order JSON
    items = OrderItemSerializer(many=True, read_only=True)
    
    # Expose your model properties to the API
    total_value = serializers.ReadOnlyField()
    total_items_count = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = [
            'invoice_no', 'customer_id', 'invoice_date', 'country', 
            'order_status', 'total_value', 'total_items_count', 'items'
        ]