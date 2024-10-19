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

### 1. **Product Update API View** (`UpdateAPIView`)

```python
# views.py
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # Lookup by primary key
    permission_classes = [AllowAny]  # No authentication required

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title  # Set content to title if not provided

product_update_view = ProductUpdateAPIView.as_view()

# Usage Example
import requests

endpoint = "http://localhost:8000/api/products/1/update"
data = {
    "title": "Hello world, my old friend",
    "price": 124.77,
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())

# Expected Output Example
# {'title': 'Hello world, my old friend', 'content': 'Hello world, my old friend', 'price': '124.77', 'sale_price': '99.82', 'my_discount': '122'}
```

### 2. **Product Destroy API View** (`DestroyAPIView`)

```python
# views.py
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]  # No authentication required

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_delete_view = ProductDestroyAPIView.as_view()

# Usage Example
import requests

product_id = input("What is the product id?")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/destroy/"
    
get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code == 204)
```

### 3. **Authentication and Permissions Explanation**

- **Authentication Classes**:
  - `authentication.SessionAuthentication`: Uses Django's session framework, allowing logged-in users to access the API. This is used for logged-in users via the Django admin panel or a frontend login.
  
- **Permission Classes**:
  - `permissions.IsAuthenticatedOrReadOnly`: Allows only authenticated users to modify data (POST, PUT, DELETE). Unauthenticated users can only read data (GET requests).

### 4. **Using `DjangoModelPermissions`**

- **`permissions.DjangoModelPermissions`**: This ensures that users have specific permissions to view, add, change, or delete objects based on the model-level permissions assigned in Django's admin.

#### Example Setup:
1. **Create a new user**:
   - Assign the user `view_product` permission.
   - The user can only view products but cannot edit or delete them.

2. **Create a new group (e.g., "Product Editor")**:
   - Assign `change_product` and `add_product` permissions.
   - Any user in this group can edit and add new products, but cannot delete them.

3. **Superuser**:
   - Has full permissions to view, edit, delete, and add products.

### 5. **Permissions in Code Example**:

```python
# views.py
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]  # Only users with proper permissions can access
```

### Example Images:
![image](https://github.com/user-attachments/assets/a3b5ffc5-bcac-4d3c-b2f4-ed92330980b1)

![image](https://github.com/user-attachments/assets/01c6c26d-3cc3-4c7a-9a7a-9394b2045bdc)

This setup allows for a secure, permission-based access model where different users have different levels of access based on their role or group in the Django admin.

---
# Permissions
**"Authentication or identification by itself is not usually sufficient to gain access to information or code. For that, the entity requesting access must have authorization."**  
— *— Apple Developer Documentation, "REST worst practices"*


### Key Concepts:
1. **Permissions**:
   - Permissions decide if a user can access a resource.
   - They work after authentication but before the view's logic is executed.
   - Permissions check the `request.user` and `request.auth` properties.
  
2. **Permission Classes**:
   - Permissions are defined as a list of classes, each checking whether a request is allowed.
   - If any permission fails, a 403 Forbidden or 401 Unauthorized error is raised.

3. **Common Permission Classes**:
   - `AllowAny`: Allows unrestricted access.
   - `IsAuthenticated`: Allows access only to authenticated users.
   - `IsAdminUser`: Only allows admin users (users with `is_staff=True`).
   - `IsAuthenticatedOrReadOnly`: Grants full access to authenticated users but read-only access to unauthenticated users.

4. **Object-level Permissions**:
   - Applied to individual objects (e.g., model instances) to check if a user has permissions to act on them.
   - Implemented by overriding the `has_object_permission()` method in custom permission classes.

5. **Custom Permissions**:
   - You can create custom permission classes by subclassing `BasePermission` and implementing `.has_permission()` or `.has_object_permission()` methods.

6. **Setting Permissions**:
   - You can set permissions globally in the `DEFAULT_PERMISSION_CLASSES` setting or per view using the `permission_classes` attribute.
   - Example:  
     ```python
     from rest_framework.permissions import IsAuthenticated
     class ExampleView(APIView):
         permission_classes = [IsAuthenticated]
     ```

By utilizing these permission classes and customization options, you can finely control who can access or modify specific API resources.

---

# Authentication (Pluggable)

**"Auth needs to be pluggable."**  
— *Jacob Kaplan-Moss, "REST worst practices"*

Authentication is the process of associating an incoming request with credentials, such as a user's identity or an authentication token. Permissions and throttling policies rely on these credentials to determine if a request should be granted access. REST framework provides several authentication schemes, and you can implement custom ones as needed.

- **Key Mechanism**: Authentication runs at the very start of the view process, before permissions and other checks. The `request.user` property usually contains a `User` instance, while `request.auth` holds additional authentication info, such as a token.
- **Note**: Authentication alone doesn't allow or deny a request—it just identifies the requester.

### How Authentication is Determined

Authentication schemes are specified as a list of classes. REST framework tries each class in the list and sets `request.user` and `request.auth` based on the first successful authentication. If no class authenticates, `request.user` defaults to `AnonymousUser`, and `request.auth` is set to `None`.

You can change the behavior for unauthenticated requests using the `UNAUTHENTICATED_USER` and `UNAUTHENTICATED_TOKEN` settings.

### Setting Authentication Scheme

You can set default authentication schemes globally in `DEFAULT_AUTHENTICATION_CLASSES`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

For per-view or per-viewset control, use the `authentication_classes` attribute:

```python
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)
```

### Unauthorized and Forbidden Responses

Two key response codes for denied requests:

- **HTTP 401 Unauthorized**: Must include a `WWW-Authenticate` header to indicate how the client should authenticate.
- **HTTP 403 Permission Denied**: Used when authentication succeeds but the user lacks permission.

### Authentication Schemes

#### 1. **BasicAuthentication**  
   Utilizes HTTP Basic Auth (username/password). Not recommended for production without HTTPS.

#### 2. **TokenAuthentication**  
   Token-based HTTP Auth. Useful for client-server models (e.g., mobile apps). Tokens must be included in the `Authorization` header as:

   ```plaintext
   Authorization: Token <token_key>
   ```

   To generate tokens for users:

   ```python
   from rest_framework.authtoken.models import Token
   token = Token.objects.create(user=...)
   ```

   To add an endpoint for token retrieval:

   ```python
   from rest_framework.authtoken import views
   urlpatterns += [
       path('api-token-auth/', views.obtain_auth_token)
   ]
   ```

   You can customize this behavior by subclassing `ObtainAuthToken`.

#### 3. **SessionAuthentication**  
   Uses Django's session framework. Best for AJAX clients in the same session as the website. Requires CSRF tokens for unsafe methods (e.g., `POST`, `DELETE`).

#### 4. **RemoteUserAuthentication**  
   Delegates authentication to the web server, which sets the `REMOTE_USER` environment variable. Requires `RemoteUserBackend` in `AUTHENTICATION_BACKENDS`.

#### 5. **Custom Authentication**  
   To implement custom authentication, subclass `BaseAuthentication` and override `.authenticate(self, request)`. This method should return a tuple `(user, auth)` on success or `None` on failure.
---

## Custom Permission Class: IsStaffEditorPermission

In Django REST Framework (DRF), permission classes are crucial for controlling access to views based on user roles. The `IsStaffEditorPermission` class allows only staff members to perform certain actions on a model. Here's how you can implement it:

```python
from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        # Allow access only if the user is a staff member
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)
```

- **Purpose**: The `IsStaffEditorPermission` class inherits from `DjangoModelPermissions`, which checks the permissions based on the HTTP method being used. It maps each method to specific permissions required.
  
- **Permission Mapping**: 
  - `GET` allows viewing objects.
  - `POST` allows adding new objects.
  - `PUT`, `PATCH`, and `DELETE` allow editing and deleting objects.
  
- **Custom Logic**: The `has_permission` method overrides the default permission checking to ensure that only users marked as staff can proceed with any action.

### Real-World Example

Imagine you are building an e-commerce platform where only staff members (like admins) should be allowed to add or modify products. By using this permission class, you ensure that regular users cannot access these critical functions, maintaining the integrity of your product data.

## Product List and Create API View

To utilize the custom permission class, we define a view for listing and creating products:

```python
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffEditorPermission]  # Enforce custom permission

    def perform_create(self, serializer):
        # Automatically set content if not provided
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or title
        instance = serializer.save(content=content)
```

### Explanation

- **View Class**: This class extends `ListCreateAPIView`, which provides built-in functionalities for listing and creating resources.
  
- **Permission Check**: The `permission_classes` attribute enforces the `IsStaffEditorPermission`, ensuring only staff can create or list products.

- **Creating Products**: The `perform_create` method is overridden to set the content of the product. If no content is provided, it defaults to the title.

### Solving Authorization Errors

By assigning staff roles to users, you can solve authorization errors like “You do not have permission to perform this action.” When a staff member attempts to access the view, they are granted the required permissions based on their role.

# Token Authentication

Token authentication is essential for securing APIs, allowing users to authenticate without sending their credentials with every request. Here's how you can set it up:

### Authentication Code Example

```python
import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username? \n")
password = getpass("Enter your password: \n")

# Authenticate user
auth_response = requests.post(auth_endpoint, json={"username": username, "password": password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    
    # Access protected resource
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
```

### Explanation

1. **User Input**: The script prompts the user for their username and password.
  
2. **Authentication Request**: It sends a POST request to the authentication endpoint to retrieve a token.
  
3. **Authorization Header**: If authentication is successful, it sets the `Authorization` header with the token for subsequent requests.

### Custom Token Authentication Class

You can customize the token authentication behavior as follows:

```python
from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"  # Define the keyword for token authentication

# In your settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'yourapp.authentication.TokenAuthentication',  # Include your custom authentication
    ]
}
```

### Explanation

- **Custom Keyword**: The `TokenAuthentication` class allows you to specify a custom keyword (like "Bearer") for the authorization header.

- **Settings Configuration**: You need to include your custom authentication class in the DRF settings to ensure it is used across your application.

### Update Installed Apps

Make sure to add the token authentication app to your installed apps in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken',  # Add this line
    ...
]
```

### Update API URLs

Lastly, ensure your API URLs include the authentication endpoint:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.obtain_auth_token),  # Endpoint for obtaining auth tokens
    ...
]
```

---

# Custom Validation, Permissions & Throttling

## 1. **Permission Handling with Mixins**
   In large projects, defining permission classes for each view can become repetitive. A better way to solve this is by using **mixins** for permissions. This reduces the need to repeat permission classes in every Class-Based View (CBV) or Function-Based View (FBV).

### Real-World Example:
   Think of a warehouse where only staff members can add or remove products. Instead of giving permissions to each staff member for every action (like adding a product, removing it, updating stock), you could assign a blanket permission that covers all product-related tasks.

### Implementing Permissions using Mixins:
```python
class ProductListCreateAPIView(
    StaffEditorPermissionMixin,  # Mixin for permissions
    ...
):
    pass
```

---

## 2. **Throttling: Controlling Request Rates**
Throttling limits the number of requests a user can make to an API, helping to prevent abuse. DRF provides throttling mechanisms, but in some cases, you may want to throttle the entire project using **Nginx** rather than DRF.

### Example:
   Imagine an e-commerce API where a user is allowed to make 1000 requests per day. If a user exceeds this limit, the API restricts further requests until the next day.

- **Time-Based Throttling**: You could limit users to 1000 requests per second, minute, hour, or day.

**DRF Approach**:
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day',
        'anon': '100/hour',
    }
}
```
**Nginx Approach**: Use Nginx for global throttling to ensure project-wide rate limiting.

---

## 3. **Mixins for Querysets/Serializers**
   **DRY Principle**: *Don't Repeat Yourself*. Mixins for serializers and querysets prevent redundant code. Instead of writing the same logic across multiple views, you can define a reusable block of code in a Mixin.

### Example:
```python
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # default lookup field
```

### Customizing with Mixins:
```python
class ProductGenericViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```
This eliminates the need to define the same `queryset` and `serializer_class` in every view.

---

## 4. **ViewSets and Routers**
**ViewSets** bundle together logic for handling different HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) into a single class, reducing boilerplate code.

```python
class ProductViewSet(viewsets.ModelViewSet):
    """
    get -> list (Retrieve all products)
    get -> retrieve (Product detail view)
    post -> create (Add new product)
    put -> update (Update a product)
    patch -> partial update (Partially update a product)
    delete -> destroy (Delete a product)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### Registering ViewSets with Routers:
```python
from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = router.urls
```
Routers automatically generate URLs for ViewSets, saving you from manually defining routes in `urls.py`.

---

## 5. **Custom Serializer Methods**
   You can define custom fields in your serializer using methods, giving you more control over how data is presented.

### Example of a Product Serializer:
```python
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['url', 'pk', 'title', 'content', 'price', 'sale_price', 'my_discount']

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
```

Here, `my_discount` is a custom field, and the `get_url` method generates a dynamic URL for each product.

---

## 6. **Custom Validation in Serializers**
   You can implement custom validations in DRF serializers. For example, if we want to prevent users from naming a product "Hello", we can add this restriction in the serializer.

### Example:
```python
def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError("The word 'hello' is not allowed in product titles.")
```

### Adding Custom Validation:
```python
class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[validate_title_no_hello])

    def validate_title(self, value):
        if Product.objects.filter(title__iexact=value).exists():
            raise serializers.ValidationError(f"'{value}' is already a product name.")
        return value
```
In this example, if a product title contains the word "hello", or if the title already exists, the serializer will throw a validation error.

---

## Conclusion

- **Mixins** help maintain **DRY** principles and simplify permission handling.
- **Throttling** can be controlled using DRF settings or project-wide using **Nginx**.
- **ViewSets and Routers** streamline view handling and routing in Django.
- **Custom Serializers** give flexibility for generating dynamic fields and handling complex validation.

Keep it clean, reusable, and efficient. 🎯
```


in mixin.py

class UserQuerysetMixin():
    user_field = 'user'
    allow_staff_view = False
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data ={}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and user.is_staff:
            return qs 
        return qs.filter(**lookup_data)

    def validate_title(self, value):
        request = self.context.get('request')
        user = request.user
        qs = Product.objects.filter(user=user, title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a produyct name")
        return value 


related fields and key serializer 
def get_my_user_data(self, obj):
return { "username" : obj.user.username }


from rest_framework import serializers

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)


    user = UserPublicSerializer(read_only=True)
    id = serializers.integerfield(read_only=True) #nothing model related
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        request = self.context.get('request')
        print(obj)
        user = obj
        my_products = user.product_set.all()[:5]
        return UserPRoductInlineSerizlier(qs, many=True, context = self.context).data #nested nested seralizer 

class UserProductInlinbeSerizlier(serializedrs.SEriazlier):
url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field = 'pk')
title = seriazliers.ChartField(read_only=True)



```
Here's a beautifully structured and improved Markdown guide that enhances the original content with real-world examples, readability improvements, and added explanations. The focus is on permission handling, throttling, mixins, viewsets, and serializers in Django REST Framework (DRF).

---

# 🚀 Efficient API Development with Mixins, ViewSets, Routers, and Serializers

When building APIs with Django REST Framework (DRF), **keeping your code DRY (Don't Repeat Yourself)** is crucial. One way to avoid redundancy is by using **mixins, viewsets**, and **routers**. Let’s dive into how these can make your API development more efficient!

## 🛡️ Using Permission Mixins: Simplify Permission Handling

In real-world applications, you often need to protect certain API views based on user permissions (e.g., only staff members or the resource owner can access it). Rather than setting `permission_classes` for each view, you can create a **Permission Mixin** to handle permissions globally.

### Permission Mixin Example:
```python
class StaffEditorPermissionMixin:
    permission_classes = [IsAdminUser, IsStaffEditorPermission]

    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
```

**Real-world Example:**  
Imagine a school management system where only admins and staff members can add or edit student records. This mixin can be applied to any view to enforce that only those with the correct permissions can make changes.

---

## ⚡ Throttling: Controlling API Usage with Limits

Throttling ensures that no user overloads your API with excessive requests. For example, you might limit an API to **1000 requests/day** to prevent misuse.

### DRF vs. NGINX Throttling:
- **DRF Throttling:** Ideal for specific views or user-based limits.
- **NGINX Throttling:** Handles project-wide limits and can throttle requests **at the server level** for better performance.

**Real-world Example:**  
In a public-facing e-commerce site, you'd limit how often a user can add items to their cart (to prevent bots from exploiting your system).

---

## 🛠️ DRY with Mixins for QuerySets and Serializers

### Why Mixins?  
Using mixins for QuerySets or Serializers helps avoid rewriting code across views that share similar logic. This makes your codebase cleaner and more maintainable.

### Mixin Example for QuerySet:

```python
class UserQuerysetMixin():
    user_field = 'user'
    allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {self.user_field: user}
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and user.is_staff:
            return qs
        return qs.filter(**lookup_data)
```

**Real-world Example:**  
If you have an app where users can see only their own orders (except for staff who can see all orders), this mixin can handle that logic across multiple views.

---

## 🖼️ ViewSets and Routers: Simplified Routing

DRF’s **ViewSets** combine the logic for handling multiple HTTP methods (GET, POST, PUT, DELETE) in one class, making your views more concise.

### Example: Product ViewSet
```python
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    - get -> list() -> QuerySet
    - get -> retrieve() -> Product detail
    - post -> create() -> Add new product
    - put/patch -> update() -> Update product
    - delete -> destroy() -> Remove product
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
```

### Setting up Routers for URLs:
```python
from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = router.urls
```

**Real-world Example:**  
In an online store, you could use viewsets to manage products, where **`/products/`** lists all items, and **`/products/{id}/`** retrieves details of a specific product.

---

## 🔍 Search Functionality with QuerySets

Search functionality in APIs is common when you need to filter results based on user input. You can add custom search methods using Django's `Q` object.

![image](https://github.com/user-attachments/assets/b59e35b0-e005-495e-bc97-9ec9e68652f6)

### Product Search Example:

```python
from django.db.models import Q

class ProductQuerySet(models.QuerySet):
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.filter(lookup).distinct()
        return qs
```

```python
class SearchListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Product.objects.all()
        q = self.request.GET.get('q')
        if q is not None:
            return qs.search(q)
        return qs
```

**Real-world Example:**  
Let’s say you run an anime store. A user searches for "Tanjiro" (from *Demon Slayer*). Your search view filters products by that keyword to show relevant items like figurines, posters, or apparel.

---

## 🔄 Serializers: Custom Validation and Nested Data

Serializers are key to converting complex data types like querysets into JSON and handling validation for input data.

### Custom Validation Example:

```python
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'content', 'price']

    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already taken.")
        return value
```

**Real-world Example:**  
In an inventory management system, you want to ensure no two products have the same title to avoid confusion when searching or updating items.

### Nested Serializers Example:

```python
class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'price', 'user']
```

This allows you to return user-related data along with product information in one API response.

**Real-world Example:**  
When showing product details on a marketplace, you might want to display the seller's username along with the product details.

---

## 🚀 Pagination for QuerySets

Large datasets need to be paginated to improve performance. You can set up default pagination in **`settings.py`**:

![image](https://github.com/user-attachments/assets/5d543e13-b171-4836-8518-568d89132743)

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}
```

**Real-world Example:**  
In a movie database API, showing all films in one response would overwhelm the user and server. Pagination ensures that data is served in smaller chunks, say 10 movies per page.

---
