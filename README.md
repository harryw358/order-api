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
├── order_api/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── orders/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
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

---

## 2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Apply database migrations

```
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

## Get Orders by Customer

```
GET /api/customer_orders/<customer_id>/
```

Returns all orders placed by a specific customer.

Example request:

```
GET /api/customer_orders/123/
```

Example response:

```json
[
  {
    "order_id": 489596,
    "customer_id": 123,
    "order_date": "2024-05-10",
    "total_amount": 120.50
  }
]
```

---

## Get Large Orders

```
GET /api/large_orders/
```

Returns orders with a total value above a predefined threshold.

Example request:

```
GET /api/large_orders/
```

Example response:

```json
[
  {
    "order_id": 489600,
    "customer_id": 245,
    "order_date": "2024-05-12",
    "total_amount": 820.75
  }
]
```

---

## Get Orders by Date Range

```
GET /api/orders_by_date/?start=YYYY-MM-DD&end=YYYY-MM-DD
```

Example request:

```
GET /api/orders_by_date/?start=2024-01-01&end=2024-03-01
```

Example response:

```json
[
  {
    "order_id": 489580,
    "customer_id": 121,
    "order_date": "2024-02-10",
    "total_amount": 210.00
  }
]
```

---

# Error Handling

The API uses standard HTTP status codes.

| Status Code | Meaning               |
| ----------- | --------------------- |
| 200         | Successful request    |
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
