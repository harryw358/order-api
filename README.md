# Order API

**COMP3011 - Individual Web Services API Development Project**

A RESTful Web API built with Python and Django REST Framework for managing and querying orders. This project includes an automated data import script to populate the SQLite database from a provided Excel dataset (`online_retail.xlsx`).

## Project Structure

- `manage.py` - The core Django management script.
- `store_api/` - The main Django project configuration directory.
- `orders/` - The Django app containing the API views, models, and serializers.
- `import_data.py` - A custom Python script used to parse and import data from `online_retail.xlsx` into the database.
- `db.sqlite3` - The local SQLite database.

## Prerequisites

- Python 3.8+
- `pip` (Python package manager)
- `virtualenv` (Recommended)

## Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/harryw358/order-api.git](https://github.com/harryw358/order-api.git)
   cd order-api