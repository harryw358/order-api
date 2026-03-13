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

---

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

```
GET /api/orders/
```

Returns a list of all orders stored in the database.

Example request:

```
GET /api/orders/
```

Example response:

```json
[
  {
    "order_id": "489596",
    "customer_id": "123",
    "order_date": "2024-05-10",
    "total_amount": 120.50
  }
]
```

---

## 2. Get a Specific Order

```
GET /api/orders/<order_id>/
```

Returns details for a specific order.

Example request:

```
GET /api/orders/489596/
```

Example response:

```json
{
  "order_id": "489596",
  "customer_id": "123",
  "order_date": "2024-05-10",
  "total_amount": 120.50
}
```

---

## 3. Get Orders by Customer

```
GET /api/customers/<customer_id>/orders/
```

Returns all orders belonging to a specific customer.

Example request:

```
GET /api/customers/123/orders/
```

Example response:

```json
[
  {
    "order_id": "489596",
    "customer_id": "123",
    "order_date": "2024-05-10",
    "total_amount": 120.50
  }
]
```

---

## 4. Get Large Orders

```
GET /api/orders/large/
```

Returns orders where the order value exceeds a predefined threshold.

Example request:

```
GET /api/orders/large/
```

Example response:

```json
[
  {
    "order_id": "489600",
    "customer_id": "245",
    "order_date": "2024-05-12",
    "total_amount": 820.75
  }
]
```

---

## 5. Get Orders by Date

```
GET /api/orders/date/<date>/
```

Returns all orders placed on a specific date.

Example request:

```
GET /api/orders/date/2024-02-10/
```

Example response:

```json
[
  {
    "order_id": "489580",
    "customer_id": "121",
    "order_date": "2024-02-10",
    "total_amount": 210.00
  }
]
```

---

## 6. Order Analytics Summary

```
GET /api/orders/analytics/summary/
```

Returns aggregated analytics data for orders, such as totals and counts.

Example request:

```
GET /api/orders/analytics/summary/
```

---

## 7. Advanced Order Analytics

```
GET /api/orders/analytics/advanced/
```

Provides more detailed analytics about order behaviour.

Example request:

```
GET /api/orders/analytics/advanced/
```

---

# Root Dashboard

```
GET /
```

Returns the API dashboard or homepage.

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
