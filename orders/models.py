from django.db import models

# Create your models here.

class Order(models.Model):
    """
    The high-level summary of the transaction.
    Contains data that applies to the entire purchase.
    """
    # Assuming your dataset has an Invoice Number, otherwise Django's default 'id' works.
    invoice_no = models.CharField(max_length=50, unique=True) 
    customer_id = models.CharField(max_length=50, null=True, blank=True)
    invoice_date = models.DateTimeField()
    country = models.CharField(max_length=100, default="United Kingdomp")
    order_status = models.CharField(max_length=50, default='Pending')

    class Meta:
        ordering = ['-invoice_date']

    def __str__(self):
        return f"Order {self.invoice_no} (Customer: {self.customer_id})"

    @property
    def total_value(self):
        """Dynamically calculates the total price of all items in this order."""
        # 'self.items' comes from the related_name in the OrderItem model
        return sum(item.line_total for item in self.items.all())

    @property
    def total_items_count(self):
        """Dynamically calculates the total physical quantity of items."""
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    """
    An individual line item belonging to a specific Order.
    """
    # Connects this item to a specific Order.
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    
    stock_code = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.stock_code} for Order {self.order.invoice_no}"

    @property
    def line_total(self):
        """Calculates the price for this specific row (e.g., 5 mugs @ £2.00 = £10.00)."""
        return self.quantity * self.price