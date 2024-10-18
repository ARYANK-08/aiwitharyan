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


## Understanding Django Rest Framework (DRF) Serializers with `SerializerMethodField` and Permissions

In Django Rest Framework (DRF), **serializers** play a crucial role in converting complex data types, such as querysets or model instances, into Python datatypes, which can then be easily rendered into JSON or other content types. Serializers are also used for **validating** incoming data and transforming it back into complex types.

### Key Concepts of Serializers

Here’s a walkthrough of your code, focusing on critical concepts like `SerializerMethodField`, permission classes, and how the `POST` API works.

### Example: Basic Product Serializer

#### models.py
```python
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return 122  # Dummy discount value for illustration
```

Here, you have a **`Product`** model with a calculated `sale_price` and a `get_discount` method. The `sale_price` is computed by applying a 20% discount to the price.

#### serializers.py
```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except AttributeError:
            return None
```

### 1. **Why Use Serializers Instead of `model_to_dict`?**

The `model_to_dict` method can be useful for quick serialization but lacks flexibility and validation features. Serializers provide a more powerful and structured way to manage and manipulate data, offering:

- **Field Validation**: Ensures fields have the right data types and formats.
- **Customizable Output**: Allows you to customize how specific fields are serialized (e.g., `sale_price` and `my_discount`).
- **Control Over Incoming Data**: Handles incoming data by automatically validating it.

#### Example: Why `model_to_dict` Can Miss Fields
```python
data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
```
The `model_to_dict` method won’t account for properties like `sale_price` that aren’t directly stored in the database. **Serializers** handle this by including **custom method fields** like `sale_price` or `my_discount`.

### 2. **What is `SerializerMethodField`?**

The `SerializerMethodField` is a special field type in DRF serializers that allows you to customize how a particular field is serialized by defining a method inside the serializer. It’s particularly useful for fields that are computed on the fly or for applying custom logic.

#### Example: Custom Discount Field

```python
my_discount = serializers.SerializerMethodField(read_only=True)

def get_my_discount(self, obj):
    try:
        return obj.get_discount()  # Access model method
    except AttributeError:
        return None
```
- **Purpose**: The `get_my_discount` method is used to fetch a dynamic value (`my_discount`), which doesn’t exist as a database field but is computed at runtime. 
- **Read-Only**: This field is read-only, meaning it’s not writable by API requests. It only exists for serialization purposes.

#### Real-World Example: Sales Tax Calculation

Imagine you're building an **e-commerce** application where the price displayed on the product page includes tax. However, tax isn’t stored in the database but calculated dynamically based on the user’s location:

```python
class ProductSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField(read_only=True)

    def get_final_price(self, obj):
        tax = 0.05  # 5% tax
        return obj.price * (1 + tax)
```

This allows you to send the `final_price` field as part of the serialized data, even though it doesn’t exist in the database.

### 3. **Handling API Requests**

#### views.py

```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([AllowAny])  # No permissions needed for this view
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.data
        print(data)  # Debug: Print the serialized data
    else:
        data = serializer.errors

    return Response(data)
```

- **Serializer Validation**: When you call `serializer.is_valid()`, DRF will run all field-level and method-level validations. If the incoming data is valid, it will serialize the data and return it.
- **`serializer.errors`**: If validation fails, errors are returned in a structured format.

### 4. **Permissions**

In the original view, the error occurred because of the `DjangoModelPermissionsOrAnonReadOnly` permission class, which checks permissions based on the `queryset`. This permission class works for class-based views (CBVs) but will raise issues in function-based views (FBVs) like `api_home`.

#### Solution: Use `AllowAny`

```python
@permission_classes([AllowAny])
```

This disables permission checks for this view, allowing anyone to access it.

### 5. **Form vs. Serializer**

DRF serializers are very similar to Django forms:

- **Django Forms**: Used for handling HTML form input.
- **DRF Serializers**: Used for handling API data input/output (typically JSON).

#### Example:

```python
# Django form
form = ProductForm(request.POST)

# DRF serializer
serializer = ProductSerializer(data=request.data)
```

Both validate incoming data and save it to the database if valid.

### Real-World Example: Form vs. Serializer

In a **blog application**, you’d use Django forms to create a blog post via a web interface, but you’d use serializers to accept new posts via an API.

## Understanding DRF Serializers and API Permissions

### DRF Serializers

In Django Rest Framework (DRF), **serializers** help convert complex objects (such as models) into easily manageable formats like JSON. They also validate incoming data before processing it.

### Key Concepts

- **SerializerMethodField**: Useful for dynamic data (e.g., a discount, calculated values).
- **Permissions**: Ensure only the right users can access specific views.

#### Example:
```python
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'price', 'sale_price', 'my_discount']

    def get_my_discount(self, obj):
        return obj.get_discount()  # Computed discount
```

This example dynamically calculates the `my_discount` for each product.

### Handling API Requests with Serializers

```python
@api_view(['POST'])
@permission_classes([AllowAny])
def api_home(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(serializer.errors)
```

By using serializers, your API can **validate**, **serialize**, and return **dynamic fields** like `sale_price` and `my_discount`!

--- 
Let's break down the key components of the code and improve it with explanations and real-world examples. We'll focus on **Django REST Framework's Generic API views**, **function-based views (FBVs)**, and key concepts like `GET`, `POST`, `RetrieveAPIView`, `CreateAPIView`, `ListCreateAPIView`, and `Serializer`.

---

### 1. **Using Django REST Framework's Generic API Views**

**Generic API views** in Django provide pre-built views that can handle common use cases such as fetching, creating, updating, and deleting resources. This avoids writing repetitive code.

#### Example 1: Retrieving a Product (ProductDetailAPIView)
```python
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()
```
**Explanation:**
- `RetrieveAPIView` is a generic view that automatically handles **GET** requests to retrieve a single product from the database by its primary key (`pk`).
- You specify the `queryset` (the list of objects to retrieve) and the `serializer_class` (how data should be serialized).

**Real-World Example:**
Imagine you have an e-commerce website like Amazon. When a user clicks on a product to view details, you would use a `RetrieveAPIView` to show information about that product (title, price, description, etc.).

---

#### Example 2: Creating a Product (ProductCreateAPIView)
```python
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  # No authentication required

product_create_view = ProductCreateAPIView.as_view()
```
**Explanation:**
- `CreateAPIView` handles **POST** requests, allowing new product entries to be created.
- `permission_classes = [AllowAny]` ensures no authentication is required, so any user can create a product. For production, you might want to limit this to authenticated users.

**Real-World Example:**
If you're managing a product inventory system for a store like Walmart, employees would need an interface to add new products into the system. This API view would allow adding a new product.

---

### 2. **Handling Both Listing and Creating Products (ListCreateAPIView)**

Sometimes, you want to handle both **listing** and **creating** resources in the same endpoint. This is where `ListCreateAPIView` comes into play.

```python
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Add custom logic for saving the product
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or title
        serializer.save(content=content)
```

**Explanation:**
- `ListCreateAPIView` handles both **GET** (list products) and **POST** (create a new product) requests.
- The `perform_create` method allows custom logic before saving a new product (e.g., if no `content` is provided, default it to the `title`).

**Real-World Example:**
Imagine managing a fashion store's online catalog. You might want to list all the available clothing products (GET) and also allow an admin to add new items to the store (POST).

---

### 3. **Function-Based Views (FBV) for More Flexibility**

While class-based views (CBVs) like `RetrieveAPIView` and `CreateAPIView` are great for common use cases, sometimes **function-based views (FBVs)** provide more control over request handling.

```python
@api_view(["GET", "POST"])
@permission_classes([AllowAny])  # Allow unrestricted access
def product_alt_view(request, pk=None, *args, **kwargs):
    if request.method == "GET":
        if pk is not None:
            # Detail view (fetch a single product)
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        # List view (list all products)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if request.method == "POST":
        # Create a new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "Bad data"}, status=400)
```

**Explanation:**
- `@api_view(["GET", "POST"])` makes the view handle both `GET` (retrieve product(s)) and `POST` (create product).
- If a `pk` is provided in the URL, it fetches a single product (`GET /api/products/1/`).
- If no `pk` is provided, it lists all products (`GET /api/products/`).
- It also handles `POST` requests to create a new product.

**Real-World Example:**
In a real estate app like Zillow, a user might want to view all available properties (list view), view the details of a specific property (detail view), or add a new property for sale (create view). This function-based view allows you to handle all of these use cases in one endpoint.

---

### 4. **Sending Requests with Python's `requests` Library**

Here's how to interact with these APIs using Python's `requests` library.

#### Sending a GET Request to Retrieve a Product:
```python
import requests

endpoint = "http://localhost:8000/api/products/1"
response = requests.get(endpoint)  # GET request
print(response.json())
```
**Explanation:**
- You make a GET request to retrieve a specific product by its ID (`1` in this case).

#### Sending a POST Request to Create a Product:
```python
import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "New Product",
    "price": "49.99",
}

response = requests.post(endpoint, json=data)  # POST request
print(response.json())
```
**Explanation:**
- You send a POST request to the API, passing the product data (title and price) in JSON format.

---

### 5. **Handling Errors and Authentication**

In your example, you encountered an authorization error during POST requests, which you fixed by adding:

```python
permission_classes = [AllowAny]
```

This means no authentication is required for creating a product, but for a real-world application, you might want to restrict product creation to authenticated users (e.g., admins). You could use Django REST Framework's authentication mechanisms like `IsAuthenticated` or custom permissions to handle this.

---

### Key Concepts Recap:
- **RetrieveAPIView**: Used for retrieving a single object (e.g., fetching product details).
- **CreateAPIView**: Used for creating new objects (e.g., adding a new product).
- **ListCreateAPIView**: Combines both listing and creating functionalities.
- **Function-Based Views (FBVs)**: Allow custom behavior for GET, POST, and other request methods.
- **Permission Classes**: Control access to your API views (e.g., `AllowAny` or `IsAuthenticated`).




![image](https://github.com/user-attachments/assets/cd615c48-93e4-455e-99c5-0694f85fe481)


![image](https://github.com/user-attachments/assets/8086d7bd-1cb9-47fd-9c4d-643b18ffcdfa)

---

## **Differences Between FBVs and CBVs**

| Feature                   | FBVs                                    | CBVs (Generic Views)                          |
|---------------------------|-----------------------------------------|-----------------------------------------------|
| **Code Complexity**        | Simple, straightforward for small apps | More abstract, requires understanding classes |
| **Customization**          | Full control over logic                 | Requires method overriding for customization  |
| **Code Reusability**       | Low reusability                         | High reusability (built-in logic)             |
| **Lines of Code**          | More lines                              | Less code due to DRF's built-in features      |
| **Scalability**            | Good for small projects                 | Ideal for large, scalable applications        |

---

## **When to Use What?**

### **Function-Based Views (FBVs)**
- **Small Projects**: When you have a small API with a limited number of endpoints.
- **Custom Logic**: If you have a lot of custom processing logic that doesn’t fit neatly into DRF’s generic views.

### **Class-Based Views (CBVs) / Generic Views**
- **Large, Scalable Projects**: When you’re building something complex that needs to be maintainable over time.
- **Standard CRUD Operations**: If most of your views follow standard patterns like creating, retrieving, updating, or deleting data.

---
