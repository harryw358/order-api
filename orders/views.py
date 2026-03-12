from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from django.db.models import Count, Sum
from datetime import datetime

# Create your views here.

# Handles Create (POST) and Read All (GET)
@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data) # Returns 200 OK
    
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handles Read One (GET), Update (PATCH), and Delete (DELETE)
@api_view(['GET', 'PATCH', 'DELETE'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        # partial=True allows us to just update one field, like 'order_status'
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def order_analytics(request):
    # Returns an analytics summary of store operations for management.

    # 1. Total orders in the system.
    total_orders = Order.objects.count()

    # 2. Breakdown by order status.
    status_counts = Order.objects.values('order_status').annotate(count=Count('order_status'))
    # Data formatting.
    status_breakdown = {item['order_status']: item['count'] for item in status_counts}

    # 3. Total items sitting in the store.
    items_in_store = Order.objects.filter(
        order_status__in=['Pending', 'Ready for Collection']
    ).aggregate(total_items=Sum('total_items'))['total_items'] or 0

    # Final custom JSON response.
    analytics_data = {
        "metrics": {
            "total_orders_tracked": total_orders,
            "physical_items_in_stockroom": items_in_store
        },
        "status_breakdown": status_breakdown
    }

    return Response(analytics_data)

@api_view(['GET'])
def customer_orders(request, customer_id):
    # Returns all orders associated with a specific Customer ID.

    orders = Order.objects.filter(customer_id=customer_id)

    # Return error code 404 if the customer has no orders.
    if not orders.exists():
        return Response({'message': 'No orders found for this customer.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def large_orders(request):
    # Returns orders that contain a large number of items, based on threshold set via URL query (?threshold=X).

    # Grab the threshold from the URL, default to 20.
    threshold = request.GET.get('threshold', 20)

    try:
        threshold = int(threshold)
    except ValueError:
        return Response({'error': 'Threshold must be a valid number.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Filter for orders where total_items is greater than or equal to the threshold.
    orders = Order.objects.filter(total_items__gte=threshold)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def orders_by_date(request, date_str):
    # Returns all orders palced on a specific date (Format: YYYY-MM-DD).

    try:
        # Validate that the user provided a correctly formatted date string.
        target_data = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return Response({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Django's __date lookup extracts just the date part from the DateTimeField.
    orders = Order.objects.filter(invoice_date__date=target_data)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
    