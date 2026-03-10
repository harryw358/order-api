import os
import django
import pandas as pd
from django.utils.timezone import make_aware # Added to fix timezone warnings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store_api.settings')
django.setup()

from orders.models import Order

def import_data():
    print("Loading Excel file...")
    # Bumped up to 2000 rows for a slightly larger dataset
    df = pd.read_excel('online_retail.xlsx', nrows=2000)
    
    # Filter out cancellations (invoices starting with 'C')
    df = df[~df['Invoice'].astype(str).str.startswith('C')]
    
    # Group by Invoice to aggregate the total items
    grouped = df.groupby('Invoice').agg({
        'Quantity': 'sum',
        'InvoiceDate': 'first',
        'Customer ID': 'first'
    }).reset_index()

    print(f"Found {len(grouped)} unique orders. Importing to database...")
    
    for _, row in grouped.iterrows():
        # Make the datetime timezone-aware to stop the Django warnings
        aware_date = make_aware(row['InvoiceDate'])

        Order.objects.update_or_create(
            invoice_no=str(row['Invoice']),
            defaults={
                'customer_id': str(row['Customer ID']) if pd.notna(row['Customer ID']) else 'Guest',
                'invoice_date': aware_date,
                'total_items': row['Quantity'],
                'order_status': 'Pending' 
            }
        )
    print("Import complete! No more timezone warnings.")

if __name__ == '__main__':
    import_data()