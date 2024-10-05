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

