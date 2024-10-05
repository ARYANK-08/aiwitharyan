### Django Models: Understanding Database Models in Django

In Django, **models** are essential to define the structure and behavior of the data you are storing. Each model maps to a single **database table**, and every model is represented as a Python class that subclasses `django.db.models.Model`. Each attribute of the model represents a field in the database.

Let's walk through an example of a basic Django project with models for a restaurant, users, and ratings.

---

### Model Definition Example

Here's an example of defining Django models for **Restaurants**, **Ratings**, and **Sales**:

```python
from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GK', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating: {self.rating}"

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(max_digits=8, decimal_places=2)
```

#### Explanation of Models:

- **Restaurant**: Stores details about the restaurant like name, website, date opened, coordinates (latitude, longitude), and type of cuisine. `TypeChoices` is used for selecting the restaurant type.
  
- **Rating**: Links users and restaurants. Each user can rate a restaurant. The rating is an integer between 1-5.

- **Sale**: Tracks the sales/income for each restaurant.

---

### Inserting Data into the Models

You can insert records into the database using the Django ORM. Let's see an example where we add a new restaurant:

```python
from core.models import Restaurant
from django.utils import timezone

restaurant = Restaurant()
restaurant.name = 'My Tasty Restaurant'
restaurant.latitude = 50.2
restaurant.longitude = 50.1
restaurant.date_opened = timezone.now()
restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
restaurant.website = 'https://www.letsziti.com'

restaurant.save()  # This saves the record to the database
```

This will insert a new restaurant entry into the `Restaurant` table in the database.

---

### Querying Data from Models

Django provides powerful querying options through its ORM. Here's an example of how to query all restaurants from the database:

```python
from core.models import Restaurant
from django.db import connection

restaurants = Restaurant.objects.all()
print(restaurants)
print(connection.queries)  # Outputs the SQL query Django generated
```

The result will display all restaurant entries and show the actual SQL query executed by Django:

```
<QuerySet [<Restaurant: My Tasty Restaurant>]>
[{'sql': 'SELECT "core_restaurant"."id", "core_restaurant"."name", "core_restaurant"."website", "core_restaurant"."date_opened", "core_restaurant"."latitude", "core_restaurant"."longitude", "core_restaurant"."restaurant_type" FROM "core_restaurant"', 'time': '0.001'}]
```

You can also fetch the **first restaurant** using:

```python
restaurant = Restaurant.objects.first()  # Returns the first restaurant (LIMIT 1)
```

---

### Shell Plus and Advanced Queries

Using **Django Extensions** (`shell_plus`), you can easily interact with your models:

```bash
python manage.py shell_plus --print-sql
```

With this, you'll get auto-imports of models and see the SQL queries executed during operations.

Common imports for Shell Plus:

```python
from core.models import Rating, Restaurant, Sale
from django.contrib.auth.models import User
from django.db.models import Avg, Count, F, Max, Sum
from django.utils import timezone
```

---

### Creating Records Without `.save()`

Instead of creating an object and calling `.save()`, you can use Django’s shortcut method `create()` to insert records in a single step:

```python
from core.models import Restaurant
from django.utils import timezone

Restaurant.objects.create(
    name="Pizza Shop",
    date_opened=timezone.now(),
    restaurant_type=Restaurant.TypeChoices.ITALIAN,
    latitude=20.2,
    longitude=20.1,
)
```

This will immediately insert the record into the database without needing to call `.save()`.

The generated SQL query would look like this:

```
[{'sql': 'INSERT INTO "core_restaurant" ("name", "website", "date_opened", "latitude", "longitude", "restaurant_type") VALUES (\'Pizza Shop\', \'\', \'2024-10-05\', 20.2, 20.1, \'IT\')', 'time': '0.016'}]
```

---

### Indexing and Fetching Efficiently

If you need to fetch specific records, you can index into a queryset:

```python
restaurants = Restaurant.objects.all()[0]  # Gets the first restaurant using array indexing
```



---
Here’s an improved and well-structured version of your Django ORM code with Markdown formatting, real-world examples, and simplified explanations.

---

## Django ORM Queries with Real-World Examples

This guide covers some common Django ORM queries using real-world scenarios like restaurants, ratings, and sales. By the end, you'll be able to easily perform basic database operations with Django's ORM.

---

### 1. **Counting Records**

To get the total number of **restaurants** in the database:

```python
restaurants = Restaurant.objects.count()
print(restaurants)  # Output: 2
```

- **SQL Equivalent**: `SELECT COUNT(*) FROM "core_restaurant"`
  
---

### 2. **Fetching the Last Record**

To get the **last restaurant** (based on `id` or any other sorting criteria):

```python
restaurant = Restaurant.objects.last()
print(restaurant)
```

- **SQL Equivalent**: `SELECT * FROM "core_restaurant" ORDER BY "id" DESC LIMIT 1`

---

### 3. **Working with Foreign Keys**

Let's say we have a **Rating** model where:
- **Users** can rate restaurants (1 - M relationship).
- A **restaurant** can have multiple ratings.

#### Example:

```python
restaurant = Restaurant.objects.first()  # Get the first restaurant
user = User.objects.first()              # Get the first user
Rating.objects.create(user=user, restaurant=restaurant, rating=3)
print(restaurant, user)
```

To view all **ratings**:

```python
print(Rating.objects.all())  # Output: [<Rating: Rating: 3>]
```

---

### 4. **Filtering Records**

#### Filter ratings by value:
- To find all ratings of **3 stars**:
```python
print(Rating.objects.filter(rating=3))
```
- To find all ratings of **5 stars**:
```python
print(Rating.objects.filter(rating=5))
```

#### Example: Find a restaurant by its website:
```python
restaurant = Restaurant.objects.filter(website='https://www.letsziti.com')
print(restaurant)  # Output: <QuerySet [<Restaurant: My Tasty Restaurant>]>
```

- **SQL Equivalent**: `SELECT * FROM "core_restaurant" WHERE "website" = 'https://www.letsziti.com'`

---

### 5. **Greater Than and Less Than Filters**

- **Greater than or equal to (gte)**: 
  Get ratings **greater than or equal to 3**.
  
```python
print(Rating.objects.filter(rating__gte=3))  # SQL: rating >= 3
```

- **Less than or equal to (lte)**: 
  Get ratings **less than or equal to 3**.

```python
print(Rating.objects.filter(rating__lte=3))  # SQL: rating <= 3
```

- **Exclude certain conditions**:
  
```python
print(Rating.objects.exclude(rating__lte=3))  # SQL: WHERE NOT rating <= 3
```

---

### 6. **Updating Existing Records**

To **update** an existing restaurant’s name:

```python
restaurant = Restaurant.objects.first()  # Get the first restaurant
print(restaurant)

# Update the restaurant name
restaurant.name = "Tanjiro Restaurant"
restaurant.save()

# SQL Equivalent: UPDATE "core_restaurant" SET "name" = 'Tanjiro Restaurant' WHERE "id" = 1
```

---

### 7. **Querying Related Records**

When a model has a **foreign key**, instances of the related model can be accessed via the **reverse relationship**.

#### Example:
Get the **ratings** for a restaurant using the default `rating_set` manager:

```python
restaurant = Restaurant.objects.first()
print(restaurant.rating_set.all())  # Get all ratings for the restaurant
```

You can customize this manager using `related_name`.

```python
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()
```

Now, you can use `restaurant.ratings.all()` to access all ratings for a restaurant.

---

### 8. **Creating and Querying Sales Data**

#### Defining a Sale Model:
```python
class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
```

#### Adding sales for restaurants:
```python
from django.utils import timezone

Sale.objects.create(
    restaurant=Restaurant.objects.first(),
    income=233.2,
    datetime=timezone.now()
)
Sale.objects.create(
    restaurant=Restaurant.objects.first(),
    income=23.2,
    datetime=timezone.now()
)
Sale.objects.create(
    restaurant=Restaurant.objects.first(),
    income=2.2,
    datetime=timezone.now()
)
```

To view the SQL queries generated by Django:
```python
from django.db import connection
print(connection.queries)
```

---

### 9. **Get or Create Data**

To **fetch or create** a rating record:

```python
user = User.objects.first()
restaurant = Restaurant.objects.first()

rating, created = Rating.objects.get_or_create(
    restaurant=restaurant,
    user=user,
    rating=4,
)

if created:
    # Send an email or take some action
    print(f"New rating created: {rating}")
else:
    print(f"Existing rating retrieved: {rating}")
```

- `created` is `True` if the object was created and `False` if retrieved.

---

### 10. **Summary of Query Types**

| Query Type       | Example                                                    | SQL Equivalent                                            |
|------------------|------------------------------------------------------------|-----------------------------------------------------------|
| **Count**        | `Restaurant.objects.count()`                                | `SELECT COUNT(*) FROM core_restaurant`                    |
| **Last Record**  | `Restaurant.objects.last()`                                 | `SELECT * FROM core_restaurant ORDER BY id DESC LIMIT 1`   |
| **Filter**       | `Restaurant.objects.filter(website='https://www.letsziti.com')` | `SELECT * FROM core_restaurant WHERE website = '...'`      |
| **Greater Than** | `Rating.objects.filter(rating__gte=3)`                      | `SELECT * FROM core_rating WHERE rating >= 3`             |
| **Exclude**      | `Rating.objects.exclude(rating__lte=3)`                     | `SELECT * FROM core_rating WHERE NOT rating <= 3`         |

---
