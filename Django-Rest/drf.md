# Django Rest Framework 🔥


## Working with REST APIs using `requests` and Django

This guide walks through making HTTP requests with Python's `requests` library, handling JSON responses, and creating a simple Django API endpoint. Additionally, we’ll explore how to work with model instances and convert them into API-friendly formats.

---

## Understanding HTTP Requests and Responses

### Basic HTTP Requests

When you send a request to a website, it returns a **response**. You can think of a website like a restaurant: you (the client) place an order (a request), and the kitchen (the server) sends you your meal (the response).

In the context of a REST API:
- **HTTP Request** returns data (usually in JSON) rather than a web page.
- The server processes the request and sends a structured response.

### Example: Making an API Request

```python
import requests

endpoint = "https://httpbin.org/anything"  # Test API endpoint

# Making a GET request with JSON data
data = requests.get(endpoint, json={"query": "Hello World!"})

# Print the raw text response
print(data.text)

# Convert the response to JSON format and print
print(data.json())

# Check the status code of the response
print(data.status_code)  # Status code 200 means success
```

### Key Concepts

1. **HTTP Request (REST API)**: Sends data in JSON format, often used for interacting with APIs.
2. **JSON (JavaScript Object Notation)**: A lightweight data-interchange format, similar to Python dictionaries.
    - Example: `{"query": "Hello World!"}`

### Real-World Example: Google Maps API
Imagine you're building an app that shows nearby restaurants. You can use Google Maps' API to send your location and get a JSON response with restaurant data.

---

## Form Data vs. JSON Data

When sending data in an HTTP request, you can choose between **form data** and **JSON data**.

```python
# Sending JSON data
data = requests.get(endpoint, json={"query": "Hello World!"})

# Sending form data
data = requests.get(endpoint, data={"query": "Hello World!"})
```

- **Form data** is like filling out a form on a website.
- **JSON data** is typically used when interacting with APIs.

---

## Handling Status Codes

HTTP responses come with a **status code** that tells you if your request was successful or not.

- **200**: Success (e.g., the requested data was found).
- **404**: Not Found (e.g., the server couldn’t find what you requested).
- **500**: Server Error (e.g., something went wrong on the server’s end).

```python
print(data.status_code)  # e.g., 200 (OK) or 404 (Not Found)
```

---

## Django: Building a Simple API

In Django, you can define an API endpoint using a **view function** that returns a JSON response.

### Example: Simple Django API

```python
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hello World"})
```

When you call this API endpoint, it returns a simple JSON response:

```json
{
  "message": "Hello World"
}
```

### Testing the API Locally

1. Run your Django server (`python manage.py runserver`).
2. Send a request to the API:

```python
endpoint = "http://127.0.0.1:8000/"

data = requests.get(endpoint, json={"query": "Hello World!"})
print(data.json())  # Prints: {"message": "Hello World"}
print(data.status_code)  # 200 if successful
```

---

## Returning Django Model Instances as API Responses

In a real-world application, your API might need to return data from a database. Here’s how you can do it with Django models.

### Example: Django Model to JSON Response

```python
from django.http import JsonResponse
from .models import Product  # Assuming a model 'Product'

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()  # Random product
    data = {}
    if model_data:
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)
```

### Real-World Example: E-commerce Product API
Consider a clothing store’s API. When someone requests a product, the API sends back product details like the title, description, and price.

**API Response Example**:
```json
{
  "title": "Oversized T-shirt",
  "content": "Relaxed Fit Oversized Tee",
  "price": "99.99"
}
```

---

## Django Model to Dictionary Conversion

To convert a Django model instance to a Python dictionary, use `model_to_dict`. This allows you to select specific fields from the model to return.

```python
from django.forms.models import model_to_dict

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
```

### Response Example:
```json
{
  "id": 2,
  "title": "Oversized T-shirt",
  "price": "99.99"
}
```

---

## Returning HTML Instead of JSON

If you want to return a non-JSON response (like HTML), you can use `HttpResponse`. However, converting the data to JSON manually can be cumbersome.

```python
from django.http import HttpResponse
import json

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers={"content-type": "application/json"})
```

---

## Why Use Django REST Framework (DRF)?

Manually converting data to JSON and handling HTTP responses can become repetitive. This is where Django REST Framework (DRF) comes in. DRF simplifies creating APIs by automatically serializing data and handling common tasks like validation.

---
