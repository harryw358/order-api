from django.db import models

# Create your models here.

class Order(models.Model):
    invoice_no = models.CharField(max_length=20, primary_key=True)
    customer_id = models.CharField(max_length=50, null=True, blank=True)
    invoice_date = models.DateTimeField()
    total_items = models.IntegerField(default=0)
    order_status = models.CharField(
        max_length=50,
        default='Pending',
        choices=[
            ('Pending', 'Pending'),
            ('Ready for Collection', 'Ready for Collection'),
            ('Collected', 'Collected'),
            ('Cancelled', 'Cancelled')
        ]
    )

    def __str__(self):
        return f"Order {self.invoice_no} - {self.order_status}"
