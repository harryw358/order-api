# Order API

A RESTful web API for managing customer orders.
Developed for the **COMP3011 – Web Services and Web Data** coursework at the University of Leeds.

This API provides endpoints for retrieving and analysing order data, including filtering orders by customer, identifying large orders, and retrieving orders within a date range.

---

# Features

* RESTful API built with Django REST Framework
* JSON responses for all endpoints
* Query-based analytics endpoints
* Error handling using standard HTTP status codes
* API documentation generated using Swagger / OpenAPI

---

# Tech Stack

* Python 3
* Django
* Django REST Framework
* SQLite (default Django database)
* Swagger / OpenAPI for API documentation

---

# Project Structure

```
order_api/
│
├── manage.py
├── online-retail.xlsx
├── import_data.py
├── store_api/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── orders/
    ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── orders/
│           └── index.html
│
└── docs/
    └── api_documentation.pdf
```

---

# Setup Instructions

## 1. Clone the repository

```
git clone https://github.com/harryw358/order-api.git
cd order-api
```

## 2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

---

## 2.1. Install requirements

```
pip install Django
pip install djangorestframework
pip install pandas
pip install django-cors-headers
pip install drf-spectacular
```

---

If the database already exists, steps 3 and 4 can be skipped. In the event there are changes to the root source data or changes are made to the relational model, they must be repeated.

## 3. Import online orders

```
python import_data.py
```

---


## 4. Apply database migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Run the development server

```
python manage.py runserver
```

The API will run at:

```
http://127.0.0.1:8000/
```

---

# API Endpoints

## 1. Get All Orders

Returns a list of all orders in the database including their associated items.

```
GET /api/orders/
```

Example request:

```
curl http://127.0.0.1:8000/api/orders/
```

Example response:

```json
[
  {
    "invoice_no": "1",
    "customer_id": "1",
    "country": "United Kingdom",
    "invoice_date": "2026-03-13T18:27:52.129000Z",
    "order_status": "Pending",
    "total_items_count": 2,
    "total_value": 2,
    "items": [
      {
        "id": 3836,
        "stock_code": "1",
        "description": "1",
        "quantity": 2,
        "price": "1.00",
        "line_total": 2
      }
    ]
  }
]
```

---

# CRUD Operations

## 2. Create a New Order

Creates a new order.

```
POST /api/orders/
```

Example request:

```bash
curl -X POST http://127.0.0.1:8000/api/orders/ \
-H "Content-Type: application/json" \
-d '{
  "invoice_no": "999999",
  "customer_id": "12345",
  "country": "United Kingdom",
  "order_status": "Pending"
}'
```

Response:

```
201 CREATED
```

---

## 3. Get a Specific Order

Returns details for a single order.

```
GET /api/orders/<invoice_no>/
```

Example request:

```
GET /api/orders/489597/
```

Example response:

```json
{
  "invoice_no": "489597",
  "customer_id": "Guest",
  "country": "United Kingdom",
  "invoice_date": "2009-12-01T14:28:00Z",
  "order_status": "Pending",
  "total_items_count": 25,
  "total_value": 120.75,
  "items": [
    {
      "id": 1795,
      "stock_code": "17012A",
      "description": "ORIGAMI VANILLA INCENSE/CANDLE SET",
      "quantity": 1,
      "price": "5.17",
      "line_total": 5.17
    }
  ]
}
```

---

## 4. Update an Order

Partially updates an order.

```
PATCH /api/orders/<invoice_no>/
```

Example request:

```bash
curl -X PATCH http://127.0.0.1:8000/api/orders/489597/ \
-H "Content-Type: application/json" \
-d '{"order_status":"Ready for Collection"}'
```

---

## 5. Delete an Order

Deletes an order.

```
DELETE /api/orders/<invoice_no>/
```

Example request:

```bash
curl -X DELETE http://127.0.0.1:8000/api/orders/489597/
```

Response:

```
204 NO CONTENT
```

---

# Filtering Endpoints

## 6. Get Orders by Customer

Returns all orders associated with a specific customer ID.

```
GET /api/customers/<customer_id>/orders/
```

Example:

```
GET /api/customers/17850/orders/
```

---

## 7. Get Large Orders

Returns orders that contain a large number of items.

Default threshold = **20 items**.

```
GET /api/orders/large/?threshold=<number>
```

Example:

```
GET /api/orders/large/?threshold=50
```

---

## 8. Get Orders by Date

Returns all orders placed on a specific date.

```
GET /api/orders/date/<YYYY-MM-DD>/
```

Example:

```
GET /api/orders/date/2010-12-01/
```

---

# Analytics Endpoints

## 9. Order Analytics Summary

Returns aggregated statistics about orders.

```
GET /api/orders/analytics/summary/
```

Example response:

```json
{
  "metrics": {
    "total_orders_tracked": 541,
    "physical_items_in_stockroom": 2300
  },
  "status_breakdown": {
    "Pending": 120,
    "Ready for Collection": 200,
    "Completed": 221
  }
}
```

---

## 10. Advanced Analytics

Performs advanced database analytics including revenue calculations and best-selling products.

```
GET /api/orders/analytics/advanced/
```

Example response:

```json
{
  "total_revenue": 153204.75,
  "top_5_products": [
    {
      "stock_code": "85123A",
      "description": "WHITE HANGING HEART T-LIGHT HOLDER",
      "total_sold": 2300
    }
  ],
  "country_distribution": [
    {
      "country": "United Kingdom",
      "order_count": 400
    }
  ]
}
```

# Error Handling

The API uses standard HTTP status codes.

| Status Code | Meaning               |
| ----------- | --------------------- |
| 200/201     | Successful request    |
| 400         | Bad request           |
| 404         | Resource not found    |
| 500         | Internal server error |

---

# API Documentation

Interactive API documentation is generated using Swagger.

When the server is running, documentation is available at:

```
http://127.0.0.1:8000/swagger/
```

A static version of the API documentation is also included in this repository as a PDF:

```
/docs/api_documentation.pdf
```

---

# Version Control

This project uses Git for version control. Development history and commit logs are available in the repository.

Repository:

```
https://github.com/harryw358/order-api
```

---

# Author

Harry Wray
University of Leeds
COMP3011 – Web Services and Web Data

---

# License

This project was created for academic purposes as part of a university coursework submission.
