from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

# This allows you to view/edit items directly inside the parent Order page!
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('invoice_no', 'customer_id', 'country', 'invoice_date', 'order_status')
    list_filter = ('order_status', 'country')
    search_fields = ('invoice_no', 'customer_id')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('stock_code', 'description', 'quantity', 'price', 'order')
    search_fields = ('stock_code', 'description')